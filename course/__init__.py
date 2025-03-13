import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    app.secret_key = os.getenv('SECRET_KEY','SECRET_KEY')

    db.init_app(app)

    # Flask extensions
    login_manager = LoginManager()
    login_manager.login_view = 'auth.index'
    login_manager.init_app(app)

    from .models import Student, Institution, Degree

    @login_manager.user_loader
    def load_student(student_id):
        return Student.query.get(int(student_id))

    # Blueprint register
    from course.main import main as main_bp
    app.register_blueprint(main_bp)

    from course.auth import auth as auth_bp
    app.register_blueprint(auth_bp)#, url_prefix='/auth')

    from course.students import students as student_bp
    app.register_blueprint(student_bp)
    
    return app
