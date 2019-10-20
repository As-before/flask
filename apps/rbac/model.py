# @Time    : 2019/10/20 18:19
# @Author  : Pang
# @Site    : 
# @File    : model.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from apps import app
from flask_rbac import RBAC,RoleMixin,UserMixin
db = SQLAlchemy(app)
rbac = RBAC(app)
from flask import Response

roles_parents = db.Table(
    'roles_parents',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('parent_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    parents = db.relationship(
        'Role',
        secondary=roles_parents,
        primaryjoin=(id == roles_parents.c.role_id),
        secondaryjoin=(id == roles_parents.c.parent_id),
        backref=db.backref('children', lazy='dynamic')
    )

    def __init__(self, name):
        RoleMixin.__init__(self)
        self.name = name

    def add_parent(self, parent):
        self.parents.append(parent)
        return session_commit()

    def add_parents(self, *parents):
        for parent in parents:
            self.add_parent(parent)
        return session_commit()

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()


users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=True)
    # Other columns
    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('roles', lazy='dynamic')
    )
    def add_role(self, role):
        self.roles.append(role)
        return session_commit()

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)
        return session_commit()

    def get_roles(self):
        for role in self.roles:
            yield role

def session_commit():
    try:
        db.session.commit()
    except Ellipsis as e:
        db.session.rollback()
        reason = str(e)
        return reason

if __name__=="__main__":
    subject_role = (('thrimbda', 'archon'),
                    ('probe', 'crystal_collector'),
                    ('probe', 'pylon_transporter'),
                    ('gateway', 'portal'))
    everyone = Role('everyone')
    logged_role = Role('logged_role')
    staff_role = Role('staff_role')
    other_role = Role('other_role')
    special = Role('special')

    logged_role.add_parent(everyone)
    staff_role.add_parents(everyone, logged_role)

    anonymous = User(roles=[everyone])
    normal_user = User(roles=[logged_role])
    staff_role_user = User(roles=[staff_role])
    special_user = User(roles=[special])
    many_roles_user = User(roles=[logged_role, other_role, everyone])

    current_user = anonymous

    rbac.set_user_loader(lambda: current_user)
    rbac.set_user_model(User)
    rbac.set_role_model(Role)

    @app.route('/')
    @rbac.allow(roles=['everyone'], methods=['GET'])
    def index():
        return Response('index')

    app.run()