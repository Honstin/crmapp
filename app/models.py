from datetime import datetime
from app import db, login
from flask_login import UserMixin#, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    f_name = db.Column(db.String(64), index=True, unique=False)
    l_name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Client(UserMixin,db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(32), index=True, unique=False)
    l_name = db.Column(db.String(32), index=True, unique=False)
    allergies = db.Column(db.Boolean)
    room = db.Column(db.String(32), index=True, unique=True)
    medication = db.Column(db.String(128), index=True)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))