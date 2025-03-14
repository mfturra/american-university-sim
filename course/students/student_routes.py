from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user, login_required, logout_user
from . import students
from collections import defaultdict
from flask.views import MethodView
from ..models import Institution, Degree, Student
from ..schema import InstitutionSchema, InstitutionUpdateSchema

@students.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    universities = Institution.query.all()

    if request.method == 'POST':
        command = request.form.get('command').strip().lower()
        
        if command == 'logout':
            return redirect(url_for('logout'))
        
        for university in universities:
            if command == university.uni_name.lower():
                return redirect(url_for('students.degree_opts', uni_id=university.id))
        
        if command in ['public', 'private', 'community']:
            return redirect(url_for('students.degree_opts', command=command))

    return render_template('students/index.html', 
                            name=current_user.firstname,
                            page_title = "Grasshopper Island",
                            introduction = "Welcome",
                            edu_options = "Your available options can be found below:",
                            edu_exploration = "Enter the university option that you'd like to explore.",
                            logout_option = "To logout, type 'logout'.",
                            universities=universities)


@students.route('/main/degree_opts/<string:command>/', methods=['GET', 'POST'])
@login_required
def degree_opts(command):
    normalized_command = command.lower()

    universities = Institution.query.all()
    matched_universities = [uni for uni in universities if uni.uni_type.lower() == normalized_command]
    
    degrees_by_uni = {}

    for university in matched_universities:
        degrees = Degree.query.filter_by(uni_id=university.id).all()
        degrees_by_track = defaultdict(list)
        for degree in degrees:
            degrees_by_track[degree.degree_track].append(degree)

        degrees_by_uni[university.uni_name] = degrees
        # degrees_by_track = defaultdict(list)
    
    if request.method == 'POST':
        command = request.form.get('command').strip().lower()

        if command in ['public', 'private', 'community']:
            return redirect(url_for('students.degree_opts', command=command))


    # for degree in degrees:
    #     degrees_by_track[degree.degree_track].append(degree)

    return render_template('students/university.html', 
                           universities=matched_universities,
                           degrees_by_track=degrees_by_track,
                           degrees_by_uni=degrees_by_uni, 
                           command=command)
    # return render_template('unis-index.html', universities=universities)
        
    # students.add_url_rule('/uni-admin/', view_func=InstitutionList.as_view('institution_list'))
    
    # class Institution(MethodView):
    #     @students.response(200, InstitutionSchema)
    #     def get(self, uni_id):
    #         university = Institution.query.get_or_404(uni_id)
    #         degrees = Degree.query.filter_by(uni_id=uni_id).all()
    #         degrees_by_track = defaultdict(list)
    #         for degree in degrees:
    #             degrees_by_track[degree.degree_track].append(degree)

    #         # degree_track = degrees[0].degree_track if degrees else None
    #         return render_template('university.html', university=university, degrees=degrees, degrees_by_track=degrees_by_track)

    
    students.add_url_rule('/uni-admin/<int:uni_id>/', view_func=Institution.as_view('institution_details'))

@students.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# @bp.route('/student/', methods=['GET', 'POST'])
# def student_index():
#     if request.method == 'POST':
#         command = request.form.get('command').strip().lower()
#         if command == 'public' or 'public university':
#             return redirect(url_for('options'))
#         elif command == 'private' or 'private_university':
#             return redirect(url_for('options'))
#         elif command == 'logout':
#             return '<h1>This option is unfortunately not available.' #redirect(url_for('logout'))
#         else:
#             flash('Invalid command. Please type "public", "private", or "logout" to proceed.')
#             return redirect(url_for('student_index'))
    
#     return render_template('/students/index.html',
#                     page_title = "Grasshopper Island",
#                     introduction = "Welcome Young Grasshopper!",
#                     edu_exploration = "Enter the university option that you'd like to explore.",
#                     edu_options = "Your available options are: 'Public University' or 'Private University'.",
#                     logout_option = "To logout, type 'logout'.")


# @bp.route('/student/options')
# def options():
#     if request.method == 'POST':
#         command = request.form.get('command').strip().lower()
#         if command == 'business' or 'bus':
#             return '<h1>Great selection!</h1>'#redirect(url_for('degree_tracks'))
#         elif command == 'stem' or 'science' or 'technology' or 'engineering' or 'math' or 'mathematics':
#             return '<h1>Great selection!</h1>'#redirect(url_for('degree_tracks'))
#         elif command == 'social sciences' or 'humanities':
#             return '<h1>Great selection!</h1>'#redirect(url_for('degree_tracks'))

#     return render_template('/students/university.html',
#                            uni_type="Public University",
#                            uni_intro="Here at the Island's Public University, we provide diverse programs and resources to help you achieve your goals. Join our inclusive community to prepare for a bright and impactful future!",
#                            general_tracks_intro="We have three career tracks available for you:",
#                            business_tracks="Business tracks specialize in Accounting, Economics, Finance, Marketing, Business Management.",
#                            social_sciences_tracks="Social Sciences tracks specialize English, History, Philosophy, Political Science, and Psychology.",
#                            stem_tracks="STEM tracks specialize Biology, Computer Science, Electrical Engineering, Mathematics, and Physics.",
#                            track_query="Which career track would you like to learn more about?",
#                            logout_option = "To logout, type 'logout'.")
