# @Time    : 2019/10/20 16:31
# @Author  : Pang
# @Site    : 
# @File    : route.py
# @Software: PyCharm

from apps.api.resource.UserSource import *
from apps import app
from flask_restful import Api

api = Api(app)
api.add_resource(Test, '/api/user', endpoint='api')

from flasgger import Swagger

Swagger(app)
