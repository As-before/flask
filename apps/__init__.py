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


app = Flask(__name__)

app.config.from_object('settings')
app.config["SECRET_KEY"] = "pangyd"
app.debug = True

from apps.auth.auths import Auth
auth = Auth()
jwt = JWT(app, auth.authenticate, auth.identity)

from apps.api.route import *

