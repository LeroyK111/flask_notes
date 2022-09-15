# Flask框架

flask，精悍简洁、可扩展强，第三方组件多。

官网：https://dormousehole.readthedocs.io/en/latest/

webFramework选择顺序：

1.fast-api：首选fast-api框架，搭建web后端服务。天生异步MVC框架。

2.Flask：同步MVC框架，轻量级别。

3.django：同步MVT框架，重武器，有你想要的一切。

4.Toronto：异步MVT框架，老牌异步web框架，其中的ioloop内核，经常被拿来单独使用。

## 目录结构

```
# 安装
pip install flask
```

```
基本目录
App.py- 主文件，配置各种全局参数
      |
    ---static 静态文件css js files等
	---templates 模板文件 html
	---routers 子路由
	---
```

### 常用依赖

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) 用于实现 WSGI ，应用和服务之间的标准 Python 接口。
- [Jinja](https://palletsprojects.com/p/jinja/) 用于渲染页面的模板语言。
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注入攻击。
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
- [Click](https://palletsprojects.com/p/click/) 是一个命令行应用的框架。用于提供 `flask` 命令，并允许添加自定义 管理命令。
- [Blinker](https://pythonhosted.org/blinker/)异步信号库，帮助实现功能解耦
- [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供快速高效的重载。
- [greenlet](https://greenlet.readthedocs.io/en/latest/)异步网关

## 快速上手

### 基础路由

#### 路由传参

### 路由跳转

### 请求头request

### jinja模板渲染



### SSR静态文件代理

### 响应头response

#### 自定义响应



### 文件上下传











### 常用响应内容的类型

https://www.runoob.com/http/http-content-type.html

![image-20220915231838323](readme.assets/image-20220915231838323.png)

![image-20220915231825204](readme.assets/image-20220915231825204.png)











代理静态文件，巨坑。

![image-20220915213031302](readme.assets/image-20220915213031302.png)



## 同步网关

已自动安装。







## jinja2模板

```
pip i jinja2
```

这里我们忽略模板，因为前后端分离的必要性。



## 内部解耦信号

```
pip install blinker
```

## 异步网关

```
pip i greenlet
```

