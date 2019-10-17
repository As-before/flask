# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   settings
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

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '000000'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5
