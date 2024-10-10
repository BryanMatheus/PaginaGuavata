from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email, password=password).first()

        if user:
            login_user(user)
            flash("Login successful!", "success")
            
            if user.rol == 'admin':
                return redirect(url_for('auth.administrador'))
            
        flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template("/users/login.html")

@auth_bp.route('/administrador')
def administrador():
    return render_template("/administradores/indexg.html")

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
