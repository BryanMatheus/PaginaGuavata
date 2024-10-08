from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)    
    app.config.from_object('config.Config')

    from app.routes import galeriaRoutes
    app.register_blueprint(galeriaRoutes.bp)
   
    return app