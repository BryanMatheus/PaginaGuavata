from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from app.models.contactanos import Contactanos

bp = Blueprint('contactanos', __name__)

@bp.route('/contactanos')
def index():
    data = Contactanos.query.all()
    return render_template('contactanos/index.html', data=data)

@bp.route('/addcontacto', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombrecon = request.form['nombrecon']
        correocon = request.form['correocon']
        r1 = request.form['r1']
        r2 = request.form['r2']
        r3 = request.form['r3']
        r4 = request.form['r4']
        r5 = request.form['r5']
        comen = request.form['comen']
        
        new_contactanos = Contactanos(nombrecon=nombrecon, correocon=correocon, r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, comen=comen )
        db.session.add(new_contactanos)
        db.session.commit()
        return redirect(url_for('contactanos.index'))

    return render_template('/contactanos/add.html')

@bp.route('/deletecontactanos/<int:id>')
def delete(id):

    contactanos = Contactanos.query.get_or_404(id)

    db.session.delete(contactanos)
    db.session.commit()

    return redirect(url_for('contactanos.index'))
