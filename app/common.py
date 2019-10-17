# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   common
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


def trueReturn(data, msg):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data, msg):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }
