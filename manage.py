# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   manage
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

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app
from app import db
manager = Manager(app)


migrate = Migrate(app, db)
manager.add_command("runserver", Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
