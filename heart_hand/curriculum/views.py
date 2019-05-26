# curriculum/views.py
from flask import render_template, url_for,flash, redirect,request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import Curriculum_Item, Subjects, Curriculum
from heart_hand.curriculum.forms import CurriculumEntryForm, CurriculumItemEntryForm, SubjectEntryForm, CurriculumItemsTable, SubjectTermSelectorForm
from datetime import datetime
import sys
from flask_table import Table, Col

curriculum = Blueprint('curriculum', __name__)

# curriculum_menu
@curriculum.route('/curriculum_menu')
@login_required
def curriculum_menu():
    return render_template('curriculum_pages/curriculum_menu.html')


############################# SUBJECT VIEWS #############################
# Add subjects
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


############################# CURRICULUM VIEWS #############################
# Add Curriculum
@curriculum.route('/add_curriculum', methods=['GET','POST'])
@login_required
def add_curriculum():

    form = CurriculumEntryForm()

    if request.method == 'POST':
        if form.validate():
            the_curriculum = Curriculum(curriculum_name=request.form['curriculum_name'],curriculum_year_level=request.form['curriculum_year_level'],curriculum_description=request.form['curriculum_description'])
            form.populate_obj(the_curriculum)
            
            db.session.add(the_curriculum)
            db.session.commit()
            flash('New Curriculum was successfully added')
            return curriculum_details(the_curriculum.id)
        else:
            flash("Your form contained errors")
            return redirect(url_for('curriculum.add_curriculum'))
     
    return render_template('curriculum_pages/add_curriculum.html', form=form) 


# return curriculum details using their id
@curriculum.route("/curriculum_details/<int:id>")
@login_required
def curriculum_details(id):
    page = request.args.get('page',1,type=int)
    # return subect or 404 page (subject not found)
    print('currciulim details', file=sys.stderr)
    the_curriculum = Curriculum.query.filter_by(id=id).first_or_404()
    return render_template('curriculum_pages/curriculum_details.html',the_curriculum=the_curriculum)


# show all curriculums with hyperlinks
@curriculum.route("/show_all_curriculums")
@login_required
def show_all_curriculums():
    the_curriculums = Curriculum.query.all()
    return render_template('curriculum_pages/show_all_curriculums.html',the_curriculums=the_curriculums) 

# Update Curriculum Details
@curriculum.route('/update_curriculum/<int:id>', methods=['GET','POST'])
@login_required
def update_curriculum(id):

    form = CurriculumEntryForm()
    the_curriculum = Curriculum.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():

        the_curriculum.curriculum_name =  form.curriculum_name.data
        the_curriculum.curriculum_description = form.curriculum_description.data
        the_curriculum.curriculum_year_level = form.curriculum_year_level.data
        db.session.commit()
        flash('Curriculum Details Updated!')
        return curriculum_details(id)

    elif request.method == "GET":
        form.curriculum_name.data = the_curriculum.curriculum_name
        form.curriculum_year_level.data = the_curriculum.curriculum_year_level
        form.curriculum_description.data = the_curriculum.curriculum_description
    return render_template('curriculum_pages/update_curriculum.html',form=form)


############################# CURRICULUM ITEM VIEWS #############################
# Add Curriculum Item
@curriculum.route("/add_curriculum_item/<int:curriculum_id>", methods=['GET','POST'])
@login_required
def add_curriculum_item(curriculum_id):

    form = CurriculumItemEntryForm()
    

    if request.method == 'POST':

        if form.validate():
            the_curriculum_item = Curriculum_Item(curriculum_id=curriculum_id,subject=request.form['subject'],term=request.form['term'],topic=request.form['topic']
                                    ,learnt_skill=request.form['learnt_skill'],concepts=request.form['concepts'],activity=request.form['activity']
                                    ,resources=request.form['resources'],sample_to_colect=request.form['sample_to_collect'],information_recorded=request.form['information_recorded']
                                    ,notes=request.form['notes'])
            
            form.populate_obj(the_curriculum_item)
            db.session.add(the_curriculum_item)
            db.session.commit()
            flash('New Curriculum Item was successfully added')
            return curriculum_item_details(the_curriculum_item.id)
        else:
            flash("Your form contained errors")
            return redirect(url_for('curriculum.add_curriculum_item',curriculum_id_id=curriculum_id))
    print('get fucked', file=sys.stderr) 
    return render_template('curriculum_pages/add_curriculum_item.html', curriculum_id=curriculum_id, form=form) 


# return curriculum item details using their id
@curriculum.route("/curriculum_item_details/<int:id>")
@login_required
def curriculum_item_details(id):
    page = request.args.get('page',1,type=int)
    # return subect or 404 page (subject not found)
    print('currciulim item details', file=sys.stderr)
    the_curriculum_item = Curriculum_Item.query.filter_by(id=id).first_or_404()
    return render_template('curriculum_pages/curriculum_items_details.html',the_curriculum_item=the_curriculum_item)


# Update Curriculum Item Details
@curriculum.route('/update_curriculum_item/<int:id>', methods=['GET','POST'])
@login_required
def update_curriculum_item(id):

    form = CurriculumItemEntryForm()
    the_curriculum_item = Curriculum_Item.query.filter_by(id=id).first_or_404()

    
    if form.validate_on_submit():

        the_curriculum_item.subject = form.subject.data
        the_curriculum_item.topic =  form.topic.data
        the_curriculum_item.term =  form.term.data
        the_curriculum_item.learnt_skill = form.learnt_skill.data
        the_curriculum_item.concepts = form.concepts.data
        the_curriculum_item.activity = form.activity.data
        the_curriculum_item.resources = form.resources.data
        the_curriculum_item.sample_to_colect = form.sample_to_collect.data
        the_curriculum_item.information_recorded = form.information_recorded.data
        the_curriculum_item.notes = form.notes.data
        db.session.commit()
        flash('Curriculum Item Details Updated!')
        return curriculum_item_details(id)

    elif request.method == "GET":
        form.subject.data = the_curriculum_item.subject
        form.topic.data = the_curriculum_item.topic
        form.term.data = the_curriculum_item.term
        form.learnt_skill.data = the_curriculum_item.learnt_skill
        form.concepts.data = the_curriculum_item.concepts
        form.activity.data = the_curriculum_item.activity 
        form.resources.data = the_curriculum_item.resources
        form.sample_to_collect.data = the_curriculum_item.sample_to_collect
        form.information_recorded.data = the_curriculum_item.information_recorded
        form.notes.data = the_curriculum_item.notes
    return render_template('curriculum_pages/update_curriculum_item.html',form=form)


# show all curriculum items with hyperlinks
@curriculum.route("/show_all_curriculum_items")
@login_required
def show_all_curriculum_items():
    the_curriculum_items = Curriculum_Item.query.all()
    return render_template('curriculum_pages/show_all_curriculum_items.html',the_curriculum_items=the_curriculum_items) 


# show table for curriculum items
@curriculum.route("/show_table")
@login_required
def show_table():
    qry = db.session.query(Curriculum_Item)
    results = qry.all()
    table = CurriculumItemsTable(results)
    table.border = True
    return render_template('curriculum_pages/curriculum_items_table.html', table=table)

# show table for selected term
@curriculum.route("/show_table_for_term/<int:term>")
@login_required
def show_table_for_term(term):
    qry = db.session.query(Curriculum_Item).filter_by(term=term)
    results = qry.all()
    table = CurriculumItemsTable(results)
    table.border = True
    return render_template('curriculum_pages/curriculum_items_table_for_term.html', term=term, table=table) 

# show table for selected term and subject
@curriculum.route("/show_table_for_term/<int:term>/<string:subject>")
@login_required
def show_table_for_term_subject(term, subject):
    qry = db.session.query(Curriculum_Item).filter_by(term=term, subject=subject)
    results = qry.all()
    table = CurriculumItemsTable(results)
    table.border = True
    new_subject = str(subject)
    page_subject = new_subject.strip('\'()\',')
    print(page_subject, file=sys.stderr)
    return render_template('curriculum_pages/curriculum_table_term_subject.html', subject=page_subject, term=term, table=table) 


# Show Curriculum Items Table for selected Term and Subject
@curriculum.route('/table_selector', methods=['GET','POST'])
@login_required
def table_selector():

    form = SubjectTermSelectorForm()
        
    if form.validate_on_submit():

        the_subject = form.subject.data
        the_term =  form.term.data
             
        return show_table_for_term_subject(the_term, the_subject)

   
    return render_template('curriculum_pages/subject_term_selector.html',form=form)
