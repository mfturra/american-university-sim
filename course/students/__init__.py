from flask import Blueprint

bp = Blueprint('students', __name__)

from course.students import routes