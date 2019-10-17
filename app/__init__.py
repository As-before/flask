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

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

app = Flask(__name__)
app.config.from_object('settings')
app.config["SECRET_KEY"] = "super-secret"
db = SQLAlchemy(app)

app.debug = True


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response


from app.auth.auths import Auth

auth = Auth()
jwt = JWT(app, auth.authenticate, auth.identity)
