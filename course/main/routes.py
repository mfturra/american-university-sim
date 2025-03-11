from flask import render_template
from course.main import bp

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')

@bp.route('/profile')
def profile():
    return 'Profile'