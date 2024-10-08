from flask import Blueprint, render_template, redirect, url_for
from app.models.galeria import Galeria
from app import db
import os

bp = Blueprint('galeria', __name__)


