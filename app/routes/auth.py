from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login exitoso!", "success")
            
            return redirect_based_on_role(user)
        
        flash('Credenciales inválidas. Por favor, intente de nuevo.', 'danger')

    return render_template("/users/users.html")


def redirect_based_on_role(usuario):
    if usuario.rol == 'admin':
        return redirect(url_for('main.vadmin'))
    elif usuario.rol == 'empleado':
        return redirect(url_for('main.vemple'))
    else:
        return redirect(url_for('main.vusuario'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))