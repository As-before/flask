# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   UserSource
  Description :
  Author :    pang
  Email   : pangyd@spsp-it.com
  date：     2019/10/20
-------------------------------------------------
  Change Activity:
          2019/10/20:
-------------------------------------------------
"""
from flask_restful import Resource
from flask import jsonify, request
from apps.api.model.model import Users
from flask_jwt import jwt_required, current_identity


class UserResource(Resource):

    @jwt_required()
    def get(self):
        """
        获取当前登录用户信息
        ---
        tags:
          - USER API
        responses:
          401:
            description: 请求失败
          200:
            description: 请求成功
            schema:
              properties:
                data:
                  type: object
                  description: 用户信息
                  default: Lua
                msg:
                  type: string
                  description: 状态信息
                status:
                  type: integer
                  description: 状态码
        """
        user = Users.get(current_identity.id)
        returnUser = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        return jsonify({
            "status": 200,
            "data": returnUser,
            "msg": "请求成功"
        })

    def post(self):
        """
        注册一个新的用户
        ---
        tags:
          - USER API
        parameters:
          - name: username
            type: string
            description: 用户名
          - name: password
            type: string
            description: 用户密码
          - name: email
            type: string
            description: 用户邮箱
        responses:
          false:
            description: 用户注册失败
            schema:
              properties:
                data:
                  type: string
                  description: 空字符串
                msg:
                  type: string
                  description: 状态信息
                status:
                  type: boolean
                  description: 状态码
          true:
            description: 用户注册成功
            schema:
              properties:
                data:
                  type: object
                  description: 用户信息
                msg:
                  type: string
                  description: 状态信息
                status:
                  type: boolean
                  description: 状态码
        """
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users(email=email, username=username, password=Users.set_password(password))
        result = Users.add(user)
        if user.id:
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            return jsonify({
                "status": True,
                "data": returnUser,
                "msg": "用户注册成功"
            })
        else:
            return jsonify({
                "status": False,
                "data": '',
                "msg": '用户注册失败'
            })

    @jwt_required()
    def delete(self):
        """
        删除用户
        ---
        tags:
          - USER API
        parameters:
          - name: username
            type: object
            description: 用户ID
        responses:
          true:
            description: 删除成功
            schema:
              properties:
                msg:
                  type: string
                  description: 状态信息
                status:
                  type: boolean
                  description: 状态码
        """
        id = request.form.get('id')
        Users.delete(id)
        return jsonify({
            "status": True,
            "msg": "删除成功"
        })

    @jwt_required()
    def put(self):
        """
        修改用户
        ---
        tags:
          - USER API
        parameters:
          - name: username
            type: string
            description: 用户名
          - name: password
            type: string
            description: 用户密码
          - name: email
            type: string
            description: 用户邮箱
        responses:
          false:
            description: 用户修改失败
            schema:
              properties:
                data:
                  type: string
                  description: 空字符串
                msg:
                  type: string
                  description: 状态信息
                status:
                  type: boolean
                  description: 状态码
          true:
            description: 用户修改成功
            schema:
              properties:
                data:
                  type: object
                  description: 用户信息
                msg:
                  type: string
                  description: 状态信息
                status:
                  type: boolean
                  description: 状态码
        """
        user = Users.get(current_identity.id)
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user.username = username
        user.email = email
        user.password = Users.set_password(password)
        Users.update()
        if user.id:
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            return jsonify({
                "status": True,
                "data": returnUser,
                "msg": "用户修改成功"
            })
        else:
            return jsonify({
                "status": False,
                "data": '',
                "msg": '用户修改失败'
            })
