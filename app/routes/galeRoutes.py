from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
from app import db
from app.models.galeria import Galeria
import os

bp = Blueprint('galeria', __name__)

@bp.route('/galeria')
def index():
    data = Galeria.query.all()
    return render_template('administradores/indexg.html', data=data)

@bp.route('/addgaleria', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descrip = request.form['descrip']
        title = request.form['title']

        imagenes = request.files['imagenes']
  
        if imagenes:
            filename = secure_filename(imagenes.filename)
            imagen_path = os.path.join('static', 'img', filename)
            imagenes.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = filename
        else:
            ruta_imagen = None
        
        new_galeria = Galeria(imagenes=ruta_imagen, descrip=descrip, title=title)
        db.session.add(new_galeria)
        db.session.commit()
        return redirect(url_for('galeria.index'))

    return render_template('/administradores/addg.html') 

@bp.route('/editgaleria/<int:id>', methods=['GET', 'POST'])
def edit(id):

    galeria = Galeria.query.get_or_404(id)

    if request.method == 'POST':
        galeria.descrip = request.form['descrip']
        galeria.title = request.form['title']
        db.session.commit()
        return redirect(url_for('galeria.index'))

    return render_template('/administradores/editg.html', galeria=galeria)

@bp.route('/deletegaleria/<int:id>')
def delete(id):
    galeria = Galeria.query.get_or_404(id)
    
    db.session.delete(galeria)
    db.session.commit()

    return redirect(url_for('galeria.index'))
