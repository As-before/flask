# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   error_code
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

from apps.libs.my_exception import APIException

class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class my_Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'
