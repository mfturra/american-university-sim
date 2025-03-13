from flask import request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, logout_user, login_user
from . import auth
from ..models import Student
from .. import db

@auth.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    if request.method == 'POST':
        command = request.form.get('command').strip().lower()
        if command == 'create':
            return redirect(url_for('auth.signup'))
        elif command == 'login':
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid command. Please type "create" or "login" to proceed.')
    return render_template('students/index.html',
                            page_title = "Grasshopper Island",
                            game_location = "Unknown, Massachusetts",
                            introduction = "Welcome ", 
                            sub_title = "Create Your Account",
                            call_to_action = "Please create an account or login to start your journey on Grasshopper Island!",
                            action_step = "To create your account type 'create'. To login, type 'login':")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email =     request.form.get('email')
        password =  request.form.get('password')
        command =   request.form.get('command').strip().lower()

        # route student based on their input
        if command == 'create':
            # flash("It looks like you don't have an account. Let's create one!")
            return redirect(url_for('auth.signup'))
        elif command == 'login':
            student = Student.query.filter_by(email=email).first()

            if not student or not check_password_hash(student.password, password):
                flash('Please check your login details and try again.')
                return redirect(url_for('auth.login'))
            return redirect(url_for('students.main'))
        else:
            flash('Invalid command. Please type "create" or "login" to proceed.')

    return render_template('main/login.html',
                            page_title = "Login",
                            main_title = "Grasshopper Island",
                            greeting = "Welcome Young Grasshopper!",
                            sub_title = "Create Your Account",
                            call_to_action = "Enter your login info to continue your journey through American University.",
                            login_action_step = "To login, type 'login'. If you don't have an account, create your account type 'create':")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        command = request.form.get('command').strip().lower()
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user already exists
        student = Student.query.filter_by(email=email).first()
        
        # check user input for next step
        if command == 'create':
            # check if user found to redirect to signup page
            if student:
                flash('Email address already exists')
                return redirect(url_for('auth.signup'))

            if len(password) < 7:
                flash('Password must be at least 7 characters long.')
                return redirect(url_for('auth.signup'))
            return redirect(url_for('auth.signup'))
        elif command == 'login':
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid command. Please type "create" or "login" to proceed.')
            # return redirect(url_for('create_account'))

        # create a new user with form data
        new_student = Student(firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(password, method='pbkdf2:sha256:1000000'))

        # add new user to database
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('main/login'))

    return render_template('main/signup.html',
                            page_title = "Grasshopper Island",
                            main_title = "Grasshopper Island",
                            sub_title = "Create Your Account",
                            call_to_action = "Please create an account to start your journey on Grasshopper Island!",
                            action_step = "To create your account type 'create'. To login, type 'login':")
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# # home page route
# @auth.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         command = request.form.get('command').strip().lower()
#         if command == 'create':
#             return redirect(url_for('create_account'))
#         elif command == 'login':
#             return redirect(url_for('student_login'))
#         else:
#             flash('Invalid command. Please type "create" or "login" to proceed.')

#     return render_template('main/index.html',
#                             page_title = "Grasshopper Island",
#                             game_location = "Unknown, Massachusetts",
#                             introduction = "Welcome Young Grasshopper! Grasshopper Island is a text-based game designed to simulate attending a four-year university without the expenses associated with it.  Here you'll be able to explore how small decisions about your degrees, loans types, and employment opportunities can compound to make you better or worse suited to pay off your student loan.",
#                             sub_title = "Create Your Account",
#                             call_to_action = "Please create an account or login to start your journey on Grasshopper Island!",
#                             action_step = "To create your account type 'create'. To login, type 'login':")

# @auth.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#     # acquire inputs from user
#         first_name =    request.form.get('first_name')
#         last_name =     request.form.get('last_name')
#         email =         request.form.get('email')
#         password =      request.form.get('password')
#         command =       request.form.get('command').strip().lower()

#         # check user input for next step
#         if command == 'create':
#             return redirect(url_for('create_account'))
#         elif command == 'login':
#             return redirect(url_for('student_login'))
#         else:
#             flash('Invalid command. Please type "create" or "login" to proceed.')
#             return redirect(url_for('create_account'))

# @auth.route('/login', methods=['GET', 'POST'])
# def student_login():
#     if request.method == 'POST':
#         return 

