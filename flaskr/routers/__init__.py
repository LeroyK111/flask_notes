"""
由于main中将flaskr注入到了环境中，我们选择了绝对路径解决问题。
子组件，导出对象，产生了两种方式：
1.绝对路径: os sys注入包到环境中
2.相对路径：. ..靠from . import
"""
