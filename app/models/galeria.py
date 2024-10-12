from app import db 

class Galeria(db.Model):
    __tablename__='galeria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagenes = db.Column(db.String(255))
    descrip = db.Column(db.String(100))
    title = db.Column(db.String(20))
    