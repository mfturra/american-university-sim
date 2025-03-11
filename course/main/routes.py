from course.main import bp
from flask import request, redirect, url_for, render_template, flash

@bp.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        command = request.form.get('command').strip().lower()
        if command == 'create':
            return redirect(url_for('create_account'))
        elif command == 'login':
            return redirect(url_for('student_login'))
        else:
            flash('Invalid command. Please type "create" or "login" to proceed.')

    return render_template('students/index.html',
                            page_title = "Grasshopper Island",
                            game_location = "Unknown, Massachusetts",
                            introduction = "Welcome Young Grasshopper! Grasshopper Island is a text-based game designed to simulate attending a four-year university without the expenses associated with it.  Here you'll be able to explore how small decisions about your degrees, loans types, and employment opportunities can compound to make you better or worse suited to pay off your student loan.",
                            sub_title = "Create Your Account",
                            call_to_action = "Please create an account or login to start your journey on Grasshopper Island!",
                            action_step = "To create your account type 'create'. To login, type 'login':")

@bp.route('/uni-main')
def uni_options():
    return render_template('students/universities.html')