from flask import render_template, request, redirect, url_for, flash, Blueprint
from app import db
from app.models.user import User

bp = Blueprint('register', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        rol = request.form['rol']

        contrasenas_por_defecto = {
            'admin': 'admin123',
        }
        
        # Verificar la contraseña para roles específicos
        if rol in contrasenas_por_defecto:
            if password != contrasenas_por_defecto[rol]:
                flash(f'Contraseña incorrecta para el rol de {rol}. Por favor, use la contraseña por defecto.', 'danger')
                return redirect(url_for('register.register'))
        
        new_user = User(email=email, password=password, rol=rol)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario registrado exitosamente.')
        return redirect(url_for('auth.login'))

    return render_template('/users/register.html')