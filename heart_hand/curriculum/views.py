# curriculum/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import Curriculum_Item, Subjects
from heart_hand.curriculum.forms import CurriculumEntryForm, SubjectEntryForm
from datetime import datetime
import sys

curriculum = Blueprint('curriculum', __name__)

# curriculum_menu
@curriculum.route('/curriculum_menu')
@login_required
def curriculum_menu():
    return render_template('curriculum_pages/curriculum_menu.html')


@curriculum.route('/add_subject', methods=['GET','POST'])
@login_required
def add_subject():

    form = SubjectEntryForm()

    if request.method == 'POST':
        if form.validate():
            the_subject = Subjects(subject_name=request.form['subject_name'],subject_description=request.form['subject_description'])
            form.populate_obj(the_subject)
            
            db.session.add(the_subject)
            db.session.commit()
            flash('New subject was successfully added')
            return subject_details(the_subject.id)
        else:
            flash("Your form contained errors")
            return redirect(url_for('curriculum.add_subject'))
     
    return render_template('curriculum_pages/add_subject.html', form=form) 


# return subject details using their id
@curriculum.route("/subject_details/<int:id>")
@login_required
def subject_details(id):
    page = request.args.get('page',1,type=int)
    # return subect or 404 page (subject not found)
    print('get fucked', file=sys.stderr)
    the_subject = Subjects.query.filter_by(id=id).first_or_404()
    return render_template('curriculum_pages/subject_details.html',the_subject=the_subject)


# show all subjects with hyperlinks
@curriculum.route("/show_all_subjects")
@login_required
def show_all_subjects():
    the_subjects = Subjects.query.all()
    return render_template('curriculum_pages/show_all_subjects.html',the_subjects=the_subjects) 

# Update Subject Details
@curriculum.route('/update_subject/<int:id>', methods=['GET','POST'])
@login_required
def update_subject(id):

    form = SubjectEntryForm()
    the_subject = Subjects.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():

        the_subject.subject_name =  form.subject_name.data
        the_subject.subject_description = form.subject_description.data
        db.session.commit()
        flash('Subject Details Updated!')
        return subject_details(id)

    elif request.method == "GET":
        form.subject_name.data = the_subject.subject_name
        form.subject_description.data = the_subject.subject_description
    return render_template('curriculum_pages/update_subject.html',form=form)