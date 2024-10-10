from app import db 

class Contactanos(db.Model):
    __tablename__='contactanos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrecon = db.Column(db.String(255))
    correocon = db.Column(db.String(255))
    r1 = db.Column(db.String(255))
    r2 = db.Column(db.String(255))
    r3 = db.Column(db.String(255))
    r4 = db.Column(db.String(255))
    r5 = db.Column(db.String(255))
    comen = db.Column(db.String(255))