# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   error
  Description :
  Author :    pang
  Email   : pangyd@spsp-it.com
  date：     2019/10/22
-------------------------------------------------
  Change Activity:
          2019/10/22:
-------------------------------------------------
"""
__author__ = 'pang'

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from itpms.common import return_code	# 这个return_code自己根据需要定义，也可以直接用HTTP CODE
from itpms.api.v1.order import api as order_api


def api_abort(code, message=None, **kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(message=message, **kwargs)
    return response,code


def invalid_token():
    response, code = api_abort(return_code.Unauthorized, message='invalid token')
    return response, code


def token_missing():
    response, code = api_abort(return_code.Unauthorized, message='token missed')
    return response, code


def token_expired():
    response, code = api_abort(return_code.Forbidden, message='token expired')
    return response, code


class ValidationError(ValueError):
    pass

# 简单列了一些，别的类型自己可以根据需要扩展补充

@order_api.errorhandler(ValidationError)
def validation_error(e):
    return api_abort(400, e.args[0])
