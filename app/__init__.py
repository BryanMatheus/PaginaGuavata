from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_idu):
        from .models.user import User
        return User.query.get(int(user_idu))

    from app.routes import register, galeRoutes
    app.register_blueprint(register.bp)
    app.register_blueprint(galeRoutes.bp)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app