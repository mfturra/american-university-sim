from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user
from . import students

@students.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        command = request.form.get('command').strip().lower()
        if command == 'public' or 'public university':
            return redirect(url_for('university_template'))
        elif command == 'private' or 'private_university':
            return redirect(url_for('university_template'))
        elif command == 'logout':
            return redirect(url_for('logout'))

    return render_template('students/index.html', 
                            name=current_user.firstname,
                            page_title = "Grasshopper Island",
                            introduction = "Welcome",
                            edu_exploration = "Enter the university option that you'd like to explore.",
                            edu_options = "Your available options are: 'Public University' or 'Private University'.",
                            logout_option = "To logout, type 'logout'.")

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
