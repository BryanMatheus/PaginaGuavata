from app import db 

class Contactanos(db.Model):
    __tablename__='contactanos'
    idcon = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g = db.Column(db.String(255))
    descrip = db.Column(db.String(255))
    title = db.Column(db.String(255))