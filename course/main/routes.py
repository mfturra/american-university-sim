from flask import request, redirect, url_for, flash, render_template
from course.main import bp

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        command = request.form.get('command').strip().lower()
        if command == 'create':
            return redirect(url_for('auth.signup'))
        elif command == 'login':
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid command. Please type "create" or "login" to proceed.')
    return render_template('main/index.html',
                            page_title = "Grasshopper Island",
                            game_location = "Unknown, Massachusetts",
                            introduction = "Welcome Young Grasshopper! Grasshopper Island is a text-based game designed to simulate attending a four-year university without the expenses associated with it.  Here you'll be able to explore how small decisions about your degrees, loans types, and employment opportunities can compound to make you better or worse suited to pay off your student loan.",
                            sub_title = "Create Your Account",
                            call_to_action = "Please create an account or login to start your journey on Grasshopper Island!",
                            action_step = "To create your account type 'create'. To login, type 'login':")
    # return render_template('main/index.html')

@bp.route('/profile')
def profile():
    return 'Profile'