"""
所有包文件的入口，导出的py文件，对象，模块的初始化都在这里设置。
"""
# 导入其他包的方法
import App

__doc__ = "注释"

__version__ = "1.0.0"
"""
__all__参数，只用于指定 from package import * 时，导入的包是哪些，不需要的包可以先不导入；并不影响from package import module/package、import package.module等形式的导入。
"""

# 导入其他包
__all__ = ["database", "models", "App"]


def main():
    print(f"这是文件名{__name__}")
    print(f"这是模块名{__package__}")
