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
        
        # cycle through university options and check for matches to command request
        for university in universities:
            if command == university.uni_type.lower():
                print(f"\n\nThe following command was fulfilled: {command}")
                return redirect(url_for('students.degree_opts', uni_id=university.id, command=command))
        
        # if command in ['public', 'private', 'community']:
        #     print("Command is reaching this branch")
        #     return redirect(url_for('students.degree_opts', command=command))

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
    # Pass in and normalize the user input to match with db table
    normalized_command = command.lower()

    # query all universities and pull info on solely the matched university
    universities = Institution.query.all()
    matched_universities = [uni for uni in universities if uni.uni_type.lower() == normalized_command]
    
    # create empty storage for degree elements
    degrees_by_uni = {}
    degrees_by_track = defaultdict(list)

    # identify all degrees based on the matching university
    for university in matched_universities:
        degrees = Degree.query.filter_by(uni_id=university.id).all()
        for degree in degrees:
            # pull degree_track table object and append its degree elements to a new dict
            degrees_by_track[degree.degree_track].append(degree)

        # store all degrees objects at uni at degrees_by_uni (inactive)
        degrees_by_uni[university.uni_name] = degrees

    
    if request.method == 'POST':
        selected_degree = request.form.get('degree').strip().lower()
        nav_command = request.form.get('nav-command').lower()

        # acquire all degrees that match for this university
        degrees = Degree.query.filter_by(uni_id=university.id).all()
        
        # modify degree titles to facilitate matching with user input
        matched_degrees = [degree for degree in degrees if degree.degree_name.strip().lower() == selected_degree]

        # cycle through degree objects and check for matches to degree request
        for degree in matched_degrees:
            if selected_degree == degree.degree_name.strip().lower():
                print(f"\n\nThe following command was fulfilled: {selected_degree}")
                return redirect(url_for('students.degree_select', command=command))
        

        return redirect(url_for('students.degree_select', degree=selected_degree, command=nav_command))


    return render_template('students/university.html', 
                           universities=matched_universities,
                           degrees_by_track=degrees_by_track,
                           degrees_by_uni=degrees_by_uni) 

@students.route('/main/degree_opts/<string:command>/<string:degree>/', methods=['GET', 'POST'])
@login_required
def degree_select(degree):
    # normalized_command = command.lower()
    normalized_degree = degree.lower()
    print(f"Selected degree: {normalized_degree}")


    return render_template('students.degree_detail')

    # # normalize university entry
    # universities = Institution.query.all()
    # matched_universities = [uni for uni in universities if uni.uni_type.lower() == normalized_command]

    # degree_info = None

    # for university in matched_universities:
    #     # extract all degree table objects into degrees
    #     degree_info = Degree.query.filter_by(uni_id=university.id, degree_name=normalized_degree).first()

    #     if degree_info:
    #         break
    
    # if not degree_info:
    #     return redirect(url_for('students.degree_opts', command=command))
    
    return f"This was the selected degree: {normalized_degree}" #render_template('students/degree_detail.html', degree=degree_info, university=university.uni_name)

    #     # create new degree list
    #     degrees_by_track = defaultdict(list)
    #     for degree in degrees:
    #         # add all matched degrees to their respective track
    #         degrees_by_track[degree.degree_track].append(degree)

    # if request.method == 'POST':
    #     command = request.form.get('command').strip.lower()

    #     # check whether command selection is valid
    #     if command in ['public', 'private', 'community']:

    #         # check whether degree selection is valid
    #         if degree in degrees:

    #             return redirect(url_for('students.degree_select', command=command, degree=degree))

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
