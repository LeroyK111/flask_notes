import os
import time

from flask import Flask
"""
配置全局文件
"""
# 注册cors
from flask_cors import CORS
# 直接调用，封装好的链接
from database import conn

# 原生sql方法，允许列表嵌套字典传参
from sqlalchemy import text

# 注册蓝图
from routers import auth, unplugView


def create_app(test_config=None):
    # !全局配置, instance_path可以配置flaskr.config路径，但是这里我们让他（推荐）自动寻找, 直接指定配置文件所在位置instance_path="config.py"
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

    app.config.from_mapping(
        # !这里放入密钥，对session进行加密，生产环境记得写随机数。这里。我们让config直接提供配置即可。
        # SECRET_KEY='dev',
    )

    # ?注册子路由
    app.register_blueprint(auth.bp)
    app.register_blueprint(unplugView.ug)

    if test_config is None:
        # 未测试时，自动寻找config.py文件，去加载from_mapping的缺省值
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 这里则自动载入测试配置文件
        app.config.from_mapping(test_config)

    try:
        # 与flaskr平行创建instance文件夹，放入config.py文件
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 视图结束的生命周期
    @app.teardown_appcontext
    def teardown_db(exception=None):
        # print("view被终结了")
        # 自动提交，这里如果提交失败，这里会异常
        conn.commit()

    # 主页写个测试路由
    @app.route('/')
    def hello():
        # 直接获取到配置项
        # print(app.secret_key)

        # ?绑定传参
        SQL = text("select * from users where id > :y").bindparams(y="2")
        print(SQL)

        # !原生sql可以接收冒号传参，可以多组传参
        result = conn.execute(
            text("select * from users where id > :x"), [{
                'x': "7"
            }])

        # 直接获取全部数据，一旦获取全部数据，
        # print(result.all())

        print(result.keys(), "\n---------------------")
        for row in result:
            print(row, f"{row.id}--{row.name}--{row.email}")

        # 测试视图结束生命周期
        time.sleep(3)

        return 'Hello, World!'

    @app.errorhandler(404)
    def page_not_found(e):
        # !全局404
        # 究竟判断哪个蓝图出错，还需要request.host_url判断
        return "出错了", e.code

    return app
