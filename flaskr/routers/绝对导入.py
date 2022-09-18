import sys, os

# !加入环境变量，找到routers的父亲
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# !直接指定包所在路径也可以
sys.path.append(os.path.abspath(r'D:\code\案列\Flask\flaskr'))

# 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径

from routers import test

print(sys.path)
test.demo()
"""
['d:\\code\\案列\\Flask\\flaskr\\routers', 'C:\\python\\python310.zip', 'C:\\python\\DLLs', 'C:\\python\\lib', 'C:\\python', 'C:\\python\\lib\\site-packages', 'C:\\python\\lib\\site-packages\\win32', 'C:\\python\\lib\\site-packages\\win32\\lib', 'C:\\python\\lib\\site-packages\\Pythonwin']


['d:\\code\\案列\\Flask\\flaskr\\routers', 'C:\\python\\python310.zip', 'C:\\python\\DLLs', 'C:\\python\\lib', 'C:\\python', 'C:\\python\\lib\\site-packages', 'C:\\python\\lib\\site-packages\\win32', 'C:\\python\\lib\\site-packages\\win32\\lib', 'C:\\python\\lib\\site-packages\\Pythonwin', 
'd:\\code\\案列\\Flask\\flaskr']
"""
