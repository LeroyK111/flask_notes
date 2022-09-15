#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入转义

import json
from markupsafe import escape
from flask import Flask, url_for, request, Response, render_template, make_response
# 启用安全名
from werkzeug.utils import secure_filename
from flask_cors import CORS
# !__name__告诉flask主入口文件在哪，实例化
app = Flask(__name__)
CORS(app)
"""
https://dormousehole.readthedocs.io/en/latest/quickstart.html
! powershel中设置值环境变量，然后直接依靠flaskClient 进行启动
> $env:FLASK_APP = "hello"
> flask run
* Running on http://127.0.0.1:5000/
"""
# ! 从数据库中取值的文件地址
page = "test"

# !直接装饰器设置url路径，返回值
# @app.route("/")
# def hello_world():
#     return "<H1>测试主页</H1>"


@app.route(f'/{page}')
def hello():
    return '测试动态路由页面'


"""
string（缺省值） 接受任何不包含斜杠的文本

int 接受正整数

float接受正浮点数

path 类似 string ，但可以包含斜杠

uuid 接受 UUID 字符串
"""

# !html转义，防止xss，加上路由传参
# @app.route("/<name>")
# def getName(name):
#     return f"hello, {escape(name)}"


# 限定类型的路由传参
@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(type(post_id))
    return f'Post {post_id}'


# 使用该路由进行xss攻击
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    print(subpath)
    return f'Subpath {escape(subpath)}'
    # return f"{subpath}"


# 斜杠之间的区别
@app.route('/projects/')
def projects():
    return '这里会自动补充斜杠'


@app.route('/about')
def about():
    return '这里则不会自动补充斜杠，而是重定向到404'


# 构建反向路由
@app.route('/index')
def index():
    return url_for("login", page="this is a test")


# 可以构建多重路由
@app.route("/login")
@app.route('/login/<page>')
def login(page=""):
    return f'测试一下{page}'


# # ?伪造请求,对url_for进行测试
# with app.test_request_context():
#     """
#     直接根据视图函数名，跳转到对应路由接口上
#     """
#     # 这里测试，这里直接返回要跳转的url
#     print("路由返回的url", url_for('login', page="使用伪造请求测试接口"))


# 使用特定http方法
@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        # 如果是其他数据，还需要其他数据，get_data()
        # 接收post传参，接收json参数
        print(request.get_json())
        # 直接使用字典，也会自动转义成json格式
        return {"state": "ok", "msg": u"这是post请求"}
    else:
        # 接收get传参，参数接收完毕
        print("查询到的参数:", request.args.get("data"))
        print("查询到的参数:", request.args.to_dict())
        # 使用自定义响应
        data = json.dumps({"state": "ok", "msg": u"这是GET请求"})
        res = Response(
            response=data,
            content_type="text/json; charset=utf-8",
            headers={"Cache-Control": "private"})
        return res


# !SSR服务端渲染 代理静态文件
@app.route('/')
@app.route('/home/<name>')
def home(name=None):
    # jinja2渲染模板，并且接收参数渲染，
    return render_template('index.html', name=name)


# !文件上传，设置请求类型 multipart/form-data
# *这个不够安全
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    ! 可能还需要的操作头需要通过config配置, 文件根路径，文件大小,文件扩展名
    UPLOAD_FOLDER = '/path/to/the/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

    ! 完全可以交给我celery去做
    """
    if request.method == 'POST':
        # 获取input的name字段
        file = request.files['file']
        file.save(f"static/uploads/{secure_filename(file.filename)}")
        return {"state": "ok", "msg": "上传完毕"}
    else:
        return {"state": 1, "msg": "这里不能使用get"}


# 下载
@app.route('/download/1.zip', methods=['GET'])
# 图片还是会自动展示，浏览器不会下载
def download_file():
    # 使用二进制
    with open("./static/uploads/1.zip", mode="rb") as f:
        data = f.read()
    return Response(response=data, content_type="application/octet-stream")


"""
cookie的验证和使用
"""
# @app.route("")

if __name__ == '__main__':
    # ! 这里我们选择python脚本启动，可以设置ip和port
    app.run(debug=True)
