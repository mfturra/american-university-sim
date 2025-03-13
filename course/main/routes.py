from flask import request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from . import main


@main.route('/profile')
def profile():
    return 'Profile'