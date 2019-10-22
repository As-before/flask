# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   route
  Description :
  Author :    pang
  Email   : pangyd@spsp-it.com
  date：     2019/10/16
-------------------------------------------------
  Change Activity:
          2019/10/16:
-------------------------------------------------
"""
from apps.api.resource.UserSource import *
from apps import app
from flask_restful import Api

api = Api(app)
api.add_resource(UserResource, '/api/user', endpoint='api')

from flasgger import Swagger

Swagger(app)