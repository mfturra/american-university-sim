from flask import render_template, request, url_for, redirect
from collections import defaultdict
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import db, Institution, Degree, Student
import pprint

from schema import InstitutionSchema, InstitutionUpdateSchema

# from sqlalchemy import create_engine, text, select
# from sqlalchemy.orm import sessionmaker

# define Blueprint for routes
main = Blueprint('main', __name__)

## Student Workflow
@main.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@main.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)

# @main.route('/create', methods=('GET', 'POST'))
# def create_student():
#     # POST request workflow
#     if request.method == 'POST':
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         age = request.form['age']
#         student = Student(firstname=firstname,
#                           lastname=lastname,
#                           email=email,
#                           age=age)
#         db.session.add(student)
#         db.session.commit()

#         return redirect(url_for('index'))
    
#     # GET request workflow
#     return render_template('create.html')

# @main.route('/<int:student_id>/edit/', methods=('GET','POST'))
# def edit_student(student_id):
#     student = Student.query.get_or_404(student_id)

#     if request.method == 'POST':
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         age = request.form['age']

#         student.firstname = firstname
#         student.lastname = lastname
#         student.email = email
#         student.age = age

#         db.session.add(student)
#         db.session.commit()

#         return redirect(url_for('index'))

#     return render_template('edit.html', student=student)

# @main.post('/<int:student_id>/delete/')
# def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))


blp = Blueprint("institution", __name__, description="All operations on institutions")

## University Workflow 

class InstitutionList(MethodView):
    @blp.response(200, InstitutionSchema)
    def get(self):
        universities = Institution.query.all()
        return render_template('unis-index.html', universities=universities)

class Institution(MethodView):
    @blp.response(200, InstitutionSchema)
    def get(self, uni_id):
        university = Institution.query.get_or_404(uni_id)
        degrees = Degree.query.filter_by(uni_id=uni_id).all()
        degrees_by_track = defaultdict(list)
        for degree in degrees:
            degrees_by_track[degree.degree_track].append(degree)

        # degree_track = degrees[0].degree_track if degrees else None
        return render_template('university.html', university=university, degrees=degrees, degrees_by_track=degrees_by_track)

# @blp.route('/uni-admin/')
# @blp.route('/uni-admin/')
blp.add_url_rule('/uni-admin/', view_func=InstitutionList.as_view('institution_list'))
blp.add_url_rule('/uni-admin/<int:uni_id>/', view_func=Institution.as_view('institution_details'))


## Degree Workflow 
@main.route('/degrees-index/')
def deg_index():
    degrees= Degree.query.all()

    # group degrees 
    grouped_degrees = defaultdict(lambda: defaultdict(list))

    for degree in degrees:
        if degree.uni_id == 1:
            university_type = 'Public University'
        elif degree.uni_id == 2:
            university_type = 'Private University'
        elif degree.uni_id == 3:
            university_type = 'Community College'
        else: 
            continue
        
        grouped_degrees[university_type][degree.degree_track].append(degree)

    pprint.pprint(dict(grouped_degrees))

    print("Grouped Degrees Structure:")
    for university_type, degree_tracks in grouped_degrees.items():
        print(f"{university_type}:")
        for track, degrees_list in degree_tracks.items():
            degree_names = [degree.degree_name for degree in degrees_list]
            print(f"  {track}: {degree_names}")
            
    return render_template('degrees-index.html', grouped_degrees=grouped_degrees)


@main.route('/degree-index/<int:degree_id>')
def degree(degree_id):
    degrees = Degree.query.get_or_404(degree_id)
    return render_template('degree.html', degrees=degrees)

@main.route('/create-degree/', methods=('GET', 'POST'))
def create_degree():
    if request.method == 'POST':
        degree_track = request.form['degree_track']
        degree_name = request.form['degree_name']
        degree_desc = request.form['degree_desc']
        curri_diff = request.form['curriculum_difficulty']
        uni_id = request.form['uni_id']
        degree = Degree(degree_track=degree_track,
                        degree_name=degree_name,
                        degree_desc=degree_desc,
                        curriculum_difficulty=curri_diff,
                        uni_id=uni_id)
        db.session.add(degree)
        db.session.commit()
    return render_template('create-degree.html')
