from flask import Blueprint, render_template
from app.models.galeria import Galeria
from app.models.contactanos import Contactanos

bp = Blueprint('pagina', __name__)

@bp.route('/')
def inicio():
    imagenes= Galeria.query.all()
    return render_template("/pagina2/landingPage.html", imagenes=imagenes)

@bp.route('/admincon')
def admincon():
    data = Contactanos.query.all()
    return render_template("/administradores/indexc.html", data=data)

@bp.route('/admingal')
def admingal():
    data = Galeria.query.all()
    return render_template("/administradores/indexg.html", data=data)
