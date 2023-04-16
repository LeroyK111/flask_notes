"""
!生产环境使用这个
启动flker:
这里我们不设置，环境变量启动flaskr。
带参数启动：
> $env:FLASK_APP = "hello"
> flask run


!开发环境，这里我们使用
当然app.run()也行
不带参数
python .\flaskr\__main__.py
"""
import os, sys
# 导入环境变量
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flaskr import App, main

# todo 老方法
# from App import create_app

if __name__ == '__main__':
    # 调用里面的方法，但是需要把__main__.py放到外面
    main()
    # ?这里指的就是本文件夹，
    # print(__name__)
    App.create_app().run(debug=True)

    # todo 老方法
    # create_app().run(debug=True)
