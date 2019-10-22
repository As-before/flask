# Copyright 2019 The Casbin Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from werkzeug.wrappers import Request
from werkzeug.exceptions import Forbidden
from flask_jwt import encode_token,jwt_required, jwt
from apps.api.model.model import Users


class CasbinMiddleware:
    def __init__(self, app, enforcer):
        self.app = app
        self.enforcer = enforcer

    def __call__(self, environ, start_response):
        request = Request(environ)

        # 检查每个请求的权限。
        if not self.check_permission(request):
            # 未授权，返回http 403错误。
            return Forbidden()(environ, start_response)

        # 权限已通过，请转到下一个模块
        return self.app(environ, start_response)

    def check_permission(self, request):
        # 根据您的身份验证方法对其进行自定义。
        user = None
        try:
            token = str(request.headers.get('Authorization')).split(' ')[1]
            id = jwt.decode(token, "pangyd", algorithms=['HS256'])['identity']
            user = Users.get(Users, id).username
        except Exception:
            user = None
        if user is None:
            user = 'anonymous'
        path = request.path
        method = request.method
        return self.enforcer.enforce(user, path, method)
