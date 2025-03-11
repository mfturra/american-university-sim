from flask import Blueprint

auth = Blueprint('auth', __name__)

from course.auth import auth_routes