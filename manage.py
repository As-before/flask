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

from flask_script import Manager

# 初始化,__name__代表主模块名或者包

app = create_app()

manager = Manager(app=app)


if __name__ == '__main__':
    manager.run()
