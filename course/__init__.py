from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    app.secret_key = os.getenv('SECRET_KEY','SECRET_KEY')

    db.init_app(app)

    # Flask extensions placeholder

    # Blueprint register placeholder
    from course.main import bp as main_bp
    app.register_blueprint(main_bp)

    # blueprint for auth routes in app
    from course.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from course.students import bp as student_bp
    app.register_blueprint(student_bp)
    
    return app
