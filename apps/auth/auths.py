# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   auths
  Description :
  Author :    pang
  Email   : pangyd@spsp-it.com
  date：     2019/10/17
-------------------------------------------------
  Change Activity:
          2019/10/17:
-------------------------------------------------
"""
__author__ = 'pang'

from apps.api.model.model import Users
import time


def error_handler(e):
    return "Something bad happened", 400


def authenticate(username, password):
    userInfo = Users.query.filter_by(username=username).first()
    if userInfo is None:
        error_handler('找不到用户')
    else:
        if Users.check_password(userInfo.password, password):
            login_time = int(time.time())
            userInfo.login_time = login_time
            Users.update()
            return userInfo
        else:
            error_handler('密码不正确')


def identity(payload):
    ids = payload['identity']
    return Users.get(ids)
