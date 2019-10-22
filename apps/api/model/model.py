# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   model
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

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash

from apps import app

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250))
    login_time = db.Column(db.Integer)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Users(id='%s')" % self.id

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hash, password):
        return check_password_hash(hash, password)

    @staticmethod
    def get(id):
        return Users.query.filter_by(id=id).first()

    @staticmethod
    def add(user):
        db.session.add(user)
        return session_commit()

    @staticmethod
    def update():
        return session_commit()

    @staticmethod
    def delete(sid):
        Users.query.filter_by(id=sid).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
