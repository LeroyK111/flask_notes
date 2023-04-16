from flask import Blueprint, render_template, abort, Response, make_response, session, request, redirect, url_for, json

# 导入视图插件
from flask.views import View
# REST式的抽象方法
from flask.views import MethodView
"""
进行可拔插视图测试
"""

ug = Blueprint(
    'unplugView', __name__, url_prefix="/new", template_folder="templates")

# ?普通装饰器方法，
# @ug.route("/", methods=["GET", "POST"])
# def show_users():
#     return {"state": "0"}

# todo 将视图抽象成类


# 使用class将视图抽象成类
class ShowUsers(View):

    def __init__(self, *args, **kwargs) -> None:
        # !导入传参
        super().__init__()
        self.args = args
        self.kwargs = kwargs

    # 重写默认执行方法
    def dispatch_request(self):
        print(self.args, self.kwargs)
        return {"a": 1}


# !添加新的路由，并且放入视图函数，起名show_users
ug.add_url_rule('/', view_func=ShowUsers.as_view('show_users', 1, 2, b=1))


# todo
class ListView(View):
    # 可以直接设置请求方式
    methods = ["GET", "POST"]

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        print(context)
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)


class UserView(ListView):
    #! 测试继承的玩法，然后重写方法
    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return {"msg": "渲染到模板的数据"}


ug.add_url_rule('/about', view_func=UserView.as_view('about_page'))
"""
REST方法视图
"""


class UserAPI(MethodView):

    def get(self):
        # users = User.query.all()
        return {"method": "GET"}

    def post(self):
        # user = User.from_form_data(request.form)
        return {"method": "POST"}


ug.add_url_rule('/rest', view_func=UserAPI.as_view('rest'))
"""
视图拦截
"""


def user_required1(f):

    def decorator(*args, **kwargs):
        if True:
            abort(401)
        return f(*args, **kwargs)

    return decorator


# 这就是视图UserAPI.as_view('zs')设定，
view = user_required1(UserAPI.as_view('zs'))
ug.add_url_rule('/zs', view_func=view)
"""
# 挂载视图的新方法
user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
"""


# * 生命周期
@ug.before_request
def before():
    print("视图之前被调用")


@ug.after_request
def after(precedview):
    print("视图后被调用")

    # !改写视图
    # precedview = Response(response="asd")

    return precedview


@ug.teardown_request
def done(exception=None):
    print("视图终结了")


# @ug.teardown_appcontext
# def close(exception=None):
#     print("蓝图没有这个生命周期")