from datetime import timedelta

# 为了方便跨视图验证，调用一个高级方法
import functools

from flask import Blueprint, redirect, render_template, request, session, url_for, make_response

# 导出密码相关的两个包
from werkzeug.security import check_password_hash, generate_password_hash

# 直接调用，封装好的链接
from flaskr.database import conn

# 还有兼容性sql方法，不使用text
from sqlalchemy import select, insert, text, update, delete

# 使用模型
from flaskr.models import user_table

# 创建一个子路由
bp = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth',
    # 模板路径
    template_folder="templates",
    # 访问 /auth/static/index.css 即可
    static_folder="static")

# 设置sessonw密钥和过期时间
bp.secret_key = b'_5#y2L"F4213ljklnwio^&*#$*(!@#nxcnkewrQ8z\n\xec]/'
bp.permanent_session_lifetime = timedelta(days=1)


@bp.route("/", methods=["GET", "POST"])
def root():
    return "子路由根路径"


# !为了复用，我们构造了一个验证器
def login_required(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        print("我被出发了", kwargs)
        if "user" not in session:
            print(session["user"])
            return {"state": "1", "msg": "请登录"}
        print("已经把test2传入view", view.__name__)
        return view(**kwargs)

    return wrapped_view


@bp.route("/test2", methods=["GET", "POST"])
@login_required
def test2():
    return {"state": "0", "msg": "验证器"}


@bp.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        data = request.get_json()
        # 查询账户是否存在
        stmt = select(user_table).where(
            user_table.c.username == data["username"])
        result = conn.execute(stmt).all()

        if not result:
            # 不存在则创建，密码统一加密
            salt = generate_password_hash(data["password"])
            conn.execute(
                insert(user_table), [{
                    "username": data["username"],
                    "password": salt
                }])
            conn.commit()
            return {"state": "create", "msg": "创建账户成功"}
        else:
            # 根据密钥验证密码
            if check_password_hash(result[0]["password"], data["password"]):
                # 设置session
                session["user"] = data
                return {"state": "ok", "msg": "登录成功"}
            else:
                # 密码不通过
                return {"state": "1", "msg": "登录失败"}

    elif "user" in session:
        print("解析出来的名字", session["user"])

        # ?再判断是否挟带正确session，为了安全一般需要再次验证数据库，才能渲染数据
        return {"state": "ok", "msg": "验证完毕，登录成功"}

    return make_response(render_template("index.html"))


@bp.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), e.code
