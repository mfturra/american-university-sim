from flask import Blueprint, render_template, request, url_for, redirect
from models import Institution, Degree, Student

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

@main.route('/create', methods=('GET', 'POST'))
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

@main.route('/<int:student_id>/edit/', methods=('GET','POST'))
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

@main.post('/<int:student_id>/delete/')
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

## University Workflow 
@main.route('/uni-index/')
def uni_index():
    universities = Institution.query.all()
    return render_template('uni-index.html', universities=universities)

@main.route('/uni-index/<int:uni_id>/')
def university(uni_id):
    university = Institution.query.get_or_404(uni_id)
    degrees = Degree.query.filter_by(uni_id=uni_id).all()
    degree_track = degrees[0].degree_track if degrees else None
    return render_template('university.html', university=university, degrees=degrees, degree_track=degree_track)

## Degree Workflow 
@main.route('/degree-index/')
def deg_index():
    degrees= Degree.query.all()
    return render_template('degree-index.html', degrees=degrees)


@main.route('/degree-index/<int:degree_id>')
def degree(degree_id):
    degrees = Degree.query.get_or_404(degree_id)
    return render_template('degree.html', degrees=degrees)

@main.route('/create-degree/', methods=('GET', 'POST'))
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
