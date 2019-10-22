# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   run
  Description :
  Author :    pang
  Email   : pangyd@spsp-it.com
  date：     2019/10/21
-------------------------------------------------
  Change Activity:
          2019/10/21:
-------------------------------------------------
"""
__author__ = 'pang'

from authz.middleware import CasbinMiddleware
import casbin
from flask import Flask

app = Flask(__name__)

# 初始化casbin执行器，从文件加载casbin模型和策略。
# 将第二个参数更改为使用数据库。
enforcer = casbin.Enforcer("tests/authz_model.conf", "tests/authz_policy.csv")

app.wsgi_app = CasbinMiddleware(app.wsgi_app, enforcer)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
