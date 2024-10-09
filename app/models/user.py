from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    telefono = db.Column(db.Integer)
    cedula = db.Column(db.Integer)
    rol = db.Column(db.String(20)) 