from flask import request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, logout_user, login_user
from . import auth
from ..models import Student
from .. import db

@auth.route('/', methods=['GET', 'POST'])
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
                            introduction = "Welcome Young Grasshopper!", 
                            sub_title = "Create Your Account",
                            call_to_action = "Please create an account or login to start your journey on Grasshopper Island!",
                            action_step = "To create your account type 'create'. To login, type 'login':")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email =     request.form.get('email')
        password =  request.form.get('password')
        remember =  True if request.form.get('remember') else False
        command =   request.form.get('command').strip().lower()

        print(f"Command received: {command}")

        # route student based on their input
        if command == 'create':
            # flash("It looks like you don't have an account. Let's create one!")
            return redirect(url_for('auth.signup'))
        elif command == 'login':
            student = Student.query.filter_by(email=email).first()

            if not student:
                flash('No account found with that email. Please check your login details.')
                return redirect(url_for('auth.login'))
            
            if not check_password_hash(student.password, password):
                flash('Incorrect password. Please try again.')
                return redirect(url_for('auth.login'))
            
            login_user(student, remember=remember)
            return redirect(url_for('students.main'))
        else:
            flash('Invalid command. Please type "login" or "create" to proceed.')
            return redirect(url_for('auth.login'))

    return render_template('main/login.html',
                            page_title = "Login to Grasshopper Island",
                            main_title = "Grasshopper Island",
                            greeting = "Welcome Young Grasshopper!",
                            sub_title = "Create Your Account",
                            call_to_action = "Enter your login info to continue your journey through American University.",
                            login_action_step = "To login to your account, type 'login'. If you don't have an account, create your account type 'create':")

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
            
            # create a new user with form data
            new_student = Student(
                firstname=firstname, 
                lastname=lastname, 
                email=email, 
                password=generate_password_hash(password, method='pbkdf2:sha256:1000000')
                )

            # add new user to database
            db.session.add(new_student)
            db.session.commit()

            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
    
        elif command == 'login':
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid command. Please type "create" or "login" to proceed.')
            # return redirect(url_for('create_account'))

    return render_template('main/signup.html',
                            page_title = "Sign Up for Grasshopper Island",
                            main_title = "Grasshopper Island",
                            sub_title = "Create Your Account",
                            call_to_action = "Please create an account to start your journey on Grasshopper Island!",
                            action_step = "To create your account type 'create'. To login, type 'login':")