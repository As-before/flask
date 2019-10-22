## 基于flask_jwt,casbin,flask_sqlalchemy,flask_restful
----flask\
    |----apps\      # flask app应用
    |    |----rbac\     # rbac权限设计
    |    |    |----run.py
    |    |    |----authz\
    |    |    |    |----authz_model.conf
    |    |    |    |----authz_policy.csv
    |    |    |    |----middleware.py
    |    |    |----model.py     # 测试文件
    |    |----auth\     # jwt认证
    |    |    |----auths.py
    |    |    |----__init__.py
    |    |----__init__.py
    |    |----templates\        # 模板文件
    |    |    |----index.html
    |    |----api\      # restful接口
    |    |    |----route.py
    |    |    |----__init__.py
    |    |    |----model\   # 模板文件
    |    |    |    |----__init__.py
    |    |    |    |----model.py
    |    |    |----resource\    # 资源文件
    |    |    |    |----UserSource.py
    |    |    |    |----__init__.py
    |----migrations\    # 数据迁移文件
    |    |----script.py.mako
    |    |----README
    |    |----alembic.ini
    |    |----env.py
    |    |----versions\
    |----manage.py      # 入口文件
    |----settings.py    # 配置文件
    |----REMADME.md
    |----requirements.txt
