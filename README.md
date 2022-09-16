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
基本目录，自定义
App.py- 主文件，配置各种全局参数
      |
    ---static 静态文件css js files等
	---templates 模板文件 html
	---routers 子路由
	---modles 数据模型
	---XXX 其他文件夹，有需要可以自定义
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

装饰器@app.route("/")

![image-20220916141821475](readme.assets/image-20220916141821475.png)



#### 路由传参

<name>

路由传参：**get传参不一样哦**

![image-20220916142436177](readme.assets/image-20220916142436177.png)

### 内部路由跳转

url_for跳转模板

![image-20220916144437713](readme.assets/image-20220916144437713.png)

#### 重定向与异常响应

真正的重定向方法，通常与url_for结合使用

![image-20220916144731612](readme.assets/image-20220916144731612.png)



### 请求头request

![image-20220916153839001](readme.assets/image-20220916153839001.png)

### SSR静态文件代理

![image-20220916153718415](readme.assets/image-20220916153718415.png)

### 响应头response

####  基础响应

![image-20220916154619464](readme.assets/image-20220916154619464.png)

#### json特定响应

直接字典即可

![image-20220916154650352](readme.assets/image-20220916154650352.png)

#### 高级响应

自定义范围更大。

![image-20220916154806419](readme.assets/image-20220916154806419.png)

### cookie设置

![image-20220916154855523](readme.assets/image-20220916154855523.png)

### session设置

cookie唯一区别，加密和不加密的区别。

#### 原生加密方法：

![image-20220916141326615](readme.assets/image-20220916141326615.png)



#### 三方加密方式：

MD5加密

全称：MD5消息摘要算法（英语：MD5 Message-Digest Algorithm），一种被广泛使用的密码散列函数，可以产生出一个128位（16字节）的散列值（hash value），用于确保信息传输完整一致。md5加密算法是不可逆的，所以解密一般都是通过暴力穷举方法，通过网站的接口实现解密。

SHA1加密

全称： 安全哈希算法（Secure Hash Algorithm）主要适用于数字签名标准（Digital Signature Standard DSS）里面定义的数字签名算法（Digital Signature Algorithm DSA），SHA1比MD5的安全性更强。对于长度小于2^ 64位的消息，SHA1会产生一个160位的消息摘要。

HMAC加密

全称： 散列消息鉴别码 （Hash Message Authentication Code）， HMAC加密算法是一种安全的基于加密hash函数和共享密钥的消息认证协议。实现原理是用公开函数和密钥产生一个固定长度的值作为认证标识，用这个标识鉴别消息的完整性。使用一个密钥生成一个固定大小的小数据块，即 MAC，并将其加入到消息中，然后传输。接收方利用与发送方共享的密钥进行鉴别认证等。

DES加密：

全称：数据加密标准（ Data Encryption Standard ），属于对称加密算法。 DES是一个分组加密算法，典型的DES以64位为分组对数据加密，加密和解密用的是同一个算法。它的密钥长度是56位（因为每个第8 位都用作奇偶校验），密钥可以是任意的56位的数，而且可以任意时候改变。

AES加密：

全称：高级加密标准（英语：Advanced Encryption Standard），在密码学中又称Rijndael加密法，是美国联邦政府采用的一种区块加密标准。这个标准用来替代原先的DES，已经被多方分析且广为全世界所使用。

RSA加密:

全称： Rivest-Shamir-Adleman， RSA加密算法是一种非对称加密算法。在公开密钥加密和电子商业中RSA被广泛使用。它被普遍认为是目前最优秀的公钥方案之一。RSA是第一个能同时用于加密和数字签名的算法，它能够抵抗到目前为止已知的所有密码攻击。

ECC加密：

全称：椭圆曲线加密（Elliptic Curve Cryptography），ECC加密算法是一种公钥加密技术，以椭圆曲线理论为基础。利用有限域上椭圆曲线的点构成的Abel群离散对数难解性，实现加密、解密和数字签名。将椭圆曲线中的加法运算与离散对数中的模乘运算相对应，就可以建立基于椭圆曲线的对应密码体制。

UUID：

生成唯一ID。标识唯一性，通常和时间戳有关。

### 文件上下传

基于表单上传文件。

![image-20220916154032638](readme.assets/image-20220916154032638.png)



基于a标签（链接方法）下载文件。

![image-20220916154043913](readme.assets/image-20220916154043913.png)

### 日志配置

![image-20220916155024589](readme.assets/image-20220916155024589.png)





### 常用响应内容的类型

https://www.runoob.com/http/http-content-type.html

![image-20220915231838323](readme.assets/image-20220915231838323.png)

![image-20220915231825204](readme.assets/image-20220915231825204.png)











代理静态文件，巨坑。

![image-20220915213031302](readme.assets/image-20220915213031302.png)



## 同步网关

已自动安装。![image-20220916155101062](readme.assets/image-20220916155101062.png)



## 数据模型

```
pip install flask-sqlalchemy
```



## rest接口模式







## CORS跨域

https://flask-cors.readthedocs.io/en/latest/

```
pip install -U flask-cors
```

![image-20220915235016547](readme.assets/image-20220915235016547.png)

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

## 部署发布

![image-20220916143334253](readme.assets/image-20220916143334253.png)











## 常用扩展

### 开发调试

- [Flask-Script](http://www.jiege.tech/extensions/flask-script.html)
- [Flask-DebugToolbar](http://www.jiege.tech/extensions/flask-debugtoolbar.html)

### 数据模型

- [Flask-SQLAlchemy](http://www.jiege.tech/extensions/flask-sqlalchemy.html)
- [Flask-Migrate](http://www.jiege.tech/extensions/flask-migrate.html)
- [Flask-GraphQL](https://pypi.org/project/Flask-GraphQL/)

### 数据缓存

- [Flask-Cache](http://www.jiege.tech/extensions/flask-cache.html)

### `Session`

- [Flask-Session](http://www.jiege.tech/extensions/flask-session.html)

### 前后端分离的项目

- [Flask-RESTPlus](http://www.jiege.tech/extensions/flask-restplus.html)
- [Flask-JWT-Extended](http://www.jiege.tech/extensions/flask-jwt-extended.html)
- [Flask-HTTPAuth](http://www.jiege.tech/extensions/flask-httpauth.html)
- [Flask-RESTful](http://www.jiege.tech/extensions/flask-restful.html)

### 邮件发送

- [Flask-Mail](http://www.jiege.tech/extensions/flask-mail.html)

### 异步操作

- [Flask-Celery-Helper](http://www.jiege.tech/extensions/flask-celery-helper.html)

### 跨域解决

- [Flask-CORS](http://www.jiege.tech/extensions/flask-cors.html)

### 模板相关

- [Flask-Bootstrap](http://www.jiege.tech/extensions/flask-bootstrap.html)
- [Flask-Moment](http://www.jiege.tech/extensions/flask-moment.html)
- [Flask-WTF](http://www.jiege.tech/extensions/flask-wtf.html)
- [Flask-Uploads](http://www.jiege.tech/extensions/flask-uploads.html)

