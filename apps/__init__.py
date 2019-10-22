# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   __init__
  Description :
  Author :    pang
  Email   : pangyd@spsp-it.com
  date：     2019/10/16
-------------------------------------------------
  Change Activity:
          2019/10/16:
-------------------------------------------------
"""
__author__ = 'pang'

from flask import Flask
from flask_jwt import JWT

# 初始化app
app = Flask(__name__)

# 数据库配置
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask'
app.config['SQLALCHEMY_DATABASE_URI'] = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# jwt认证路由
JWT_AUTH_URL_RULE = '/login'

# 初始化casbin执行器，从文件加载casbin模型和策略。
# 将第二个参数更改为使用数据库。
from apps.rbac.authz.middleware import CasbinMiddleware
import casbin

enforcer = casbin.Enforcer("apps/rbac/authz/authz_model.conf", "apps/rbac/authz/authz_policy.csv")
app.wsgi_app = CasbinMiddleware(app.wsgi_app, enforcer)

# 加载app设置
app.config.from_object('settings')
app.config["SECRET_KEY"] = "pangyd"
app.debug = True

# 加载jwt设置
from apps.auth.auths import authenticate,identity

jwt = JWT(app, authenticate, identity)

# 加载RESTful接口
from apps.api.route import *
from apps.libs.my_exception import *
from apps.libs.error_code import *

