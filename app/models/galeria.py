from app import db 

class Galeria(db.Model):
    __tablename__='galeria'
    idgal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagenes = db.Column(db.String(255))
    descrip = db.Column(db.String(255))
    title = db.Column(db.String(255))
    