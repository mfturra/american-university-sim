import os
from dotenv import load_dotenv

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from routes import main

from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker

load_dotenv()

# database credentials
user =      os.environ.get('DB_USER')
password =  os.environ.get('DB_PASSWORD')
host =      os.environ.get('DB_HOST')
port =      os.environ.get('DB_PORT')
database =  os.environ.get('DB_DATABASE')
DB_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
    )

# engine & session configuration
# engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

# create a sessionmaker to avoid having to pass the engine each time session called
# Session = sessionmaker(engine)
def create_app():
    # app config
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///database.db"   # DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connect to Flask app to leverage all sqlalchemy capabilities
    # db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    db.init_app(app)

    app.register_blueprint(main)

    return app