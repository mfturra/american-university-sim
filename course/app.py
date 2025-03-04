import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

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

# app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///database.db"   # DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect to Flask app to leverage all sqlalchemy capabilities
db = SQLAlchemy(app)

# student class config
class Student(db.Model):
    id =            db.Column(db.Integer, primary_key=True)
    firstname =     db.Column(db.String(100), nullable=False)
    lastname =      db.Column(db.String(100), nullable=False)
    email =         db.Column(db.String(80), unique=True, nullable=False)
    age =           db.Column(db.Integer)
    created_at =    db.Column(db.DateTime(timezone=True),
                           server_default=func.now())


class Institution(db.Model):
    __tablename__ = "institutions"

    id =            db.Column(db.Integer, primary_key=True)
    inst_type =     db.Column(db.String(30), nullable=False)
    uni_name =      db.Column(db.String(30), unique=True, nullable=False)
    uni_type =      db.Column(db.String(25), unique=True, nullable=False)
    uni_welcome =   db.Column(db.String(300), unique=True, nullable=False)
    uni_cost =      db.Column(db.Float(precision=2), unique=False, nullable=False)
    degrees =       db.relationship("Degree", back_populates="institution")

class Degree(db.Model):
    __tablename__ = "degrees"

    # "unique=True" = Not duplicates
    id =                        db.Column(db.Integer, primary_key=True)
    degree_track =              db.Column(db.String(30), unique=True, nullable=False)
    degree_name =               db.Column(db.String(30), unique=True, nullable=False)
    degree_desc =               db.Column(db.String(500), unique=True, nullable=False)
    curriculum_difficulty =     db.Column(db.Float(precision=2), unique=False, nullable=False)
    uni_id =                    db.Column(db.Integer, db.ForeignKey("institutions.id"), unique=False, nullable=False)
    institution =               db.relationship("institutions", back_populates="degrees")
    
# with Session.begin() as session, session.begin():
#     # utilize a SessionTransaction object for transaction catch workflows
#     session.add(
#             text("INSERT into students (name, age) VALUES (:name, :age)"),
#             [{}, {}]
#         )
    # session.commit() automatically called

## Student Workflow
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)

@app.route('/create', methods=('GET', 'POST'))
def create_student():
    # POST request workflow
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = request.form['age']
        student = Student(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))
    
    # GET request workflow
    return render_template('create.html')

@app.route('/<int:student_id>/edit/', methods=('GET','POST'))
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = request.form['age']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

@app.post('/<int:student_id>/delete/')
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

## University Workflow 
@app.route('/uni-index/')
def uni_index():
    universities = Institution.query.all()
    return render_template('uni-index.html', universities=universities)

@app.route('/uni-index/<int:uni_id>/')
def university(uni_id):
    university = Institution.query.get_or_404(uni_id)
    return render_template('university.html', university=university)

## Degree Workflow 
@app.route('/degree-index/')
def deg_index():
    degrees= Degree.query.all()
    return render_template('degree-index.html', degrees=degrees)

@app.route('/create-degree/', methods=('GET', 'POST'))
def create_degree():
    if request.method == 'POST':
        degreetrack = request.form('degree_track')
        degreename = request.form('degree_name')
        degreedesc = request.form('degree_desc')
        curri_diff = request.form('curriculum_difficulty')
        uni_id = request.form('uni_id')
        degree = Degree(degreetrack=degreetrack,
                        degreename=degreename,
                        degreedesc=degreedesc,
                        curri_diff=curri_diff,
                        uni_id=uni_id)
        db.session.add(degree)
        db.session.commit()
    return render_template('create-degree.html')
