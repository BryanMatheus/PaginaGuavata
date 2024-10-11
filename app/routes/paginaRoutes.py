from flask import Blueprint, render_template
from app.models.galeria import Galeria

bp = Blueprint('pagina', __name__)

@bp.route('/')
def inicio():
    imagenes= Galeria.query.all()
    return render_template("/pagina2/landingPage.html", imagenes=imagenes)