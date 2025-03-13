from flask import Blueprint

students = Blueprint('students', __name__)

from . import student_routes