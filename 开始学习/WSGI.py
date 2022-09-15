#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
werkzeug用于实现 WSGI ，应用和服务之间的标准 Python 接口。
"""

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


@Request.application
def hello(Request):
    return Response("hello world")


if __name__ == '__main__':
    run_simple('localhost', 4000, hello)
