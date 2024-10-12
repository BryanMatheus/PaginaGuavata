from app import db

class Contactanos(db.Model):
    __tablename__ = 'contactanos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrecon = db.Column(db.String(30), nullable=False)
    correocon = db.Column(db.String(30), nullable=False)
    r1 = db.Column(db.String(50), nullable=True)
    r2 = db.Column(db.String(50), nullable=True)
    r3 = db.Column(db.String(50), nullable=True)
    r4 = db.Column(db.String(50), nullable=True)
    r5 = db.Column(db.String(50), nullable=True)
    comen = db.Column(db.String(100), nullable=True)
