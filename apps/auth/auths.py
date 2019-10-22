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

class Auth():

    def error_handler(self, e):
        return "Something bad happened", 400

    def authenticate(self, username, password):
        userInfo = Users.query.filter_by(username=username).first()
        if (userInfo is None):
            self.error_handler('找不到用户')
        else:
            if Users.check_password(Users, userInfo.password, password):
                login_time = int(time.time())
                userInfo.login_time = login_time
                Users.update(Users)
                return userInfo
            else:
                self.error_handler('密码不正确')

    def identity(self, payload):
        id = payload['identity']
        return Users.get(Users, id)
