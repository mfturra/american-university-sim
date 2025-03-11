from flask import Blueprint

bp = Blueprint('main', __name__)

from course.main import routes
