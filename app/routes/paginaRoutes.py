from flask import Blueprint, render_template

bp = Blueprint('pagina', __name__)

@bp.route('/')
def inicio():
    return render_template("/pagina2/landingPage.html")