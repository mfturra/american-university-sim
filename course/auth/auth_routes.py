from course.auth import auth
from flask import request, redirect, url_for, render_template, flash

@auth.route('/login')
def login():
    return render_template('main/login.html')

@auth.route('/signup')
def signup():
    return render_template('main/signup.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup_post():
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout reached!'

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

