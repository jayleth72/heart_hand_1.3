# classes/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import User, Person, Child, Lesson
from heart_hand.classes.forms import LessonEntryForm
from datetime import datetime

classes = Blueprint('classes', __name__)

# classes_menu
@classes.route('/classes_menu')
@login_required
def classes_menu():
    return render_template('classes_pages/classes_menu.html')


############################# LESSON VIEWS #############################
@classes.route('/add_lesson', methods=['GET','POST'])
@login_required
def add_lesson():

    form = LessonEntryForm()

    if request.method == 'POST':
        if form.validate():
            lesson = Lesson(lesson_name=request.form['lesson_name'],term=request.form['term'],day_of_class=request.form['day_of_class'],lesson_time=request.form['lesson_time'],lesson_duration=request.form['lesson_duration']
                       ,lesson_start_date=request.form['lesson_start_date'],lesson_cost=request.form['lesson_cost'],lesson_description=request.form['lesson_description'])
            form.populate_obj(lesson)
            
            db.session.add(lesson)
            db.session.commit()
            flash('New lesson was successfully added')
            
            return lesson_details(lesson.id)
        else:
            flash("Your form contained errors")
            return redirect(url_for('classes.add_lesson'))
     
    return render_template('classes_pages/add_lesson.html', form=form)  


# return lesson details using their id
@classes.route("/lesson_details/<int:id>")
@login_required
def lesson_details(id):
    page = request.args.get('page',1,type=int)
    # return lesson or 404 page (lesson not found)
    the_lesson = Lesson.query.filter_by(id=id).first_or_404()
    return render_template('classes_pages/lesson_details.html',the_lesson=the_lesson)


# Update lesson Details
@classes.route('/update_lesson/<int:id>', methods=['GET','POST'])
@login_required
def update_lesson(id):

    form = LessonEntryForm()
    lesson = Lesson.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():
        
        lesson.lesson_name = form.lesson_name.data 
        lesson.term = form.term.data 
        lesson.day_of_class= form.day_of_class.data 
        lesson.lesson_time = form.lesson_time.data
        lesson.lesson_duration = form.lesson_duration.data
        lesson.lesson_start_date = form.lesson_start_date.data
        lesson.lesson_cost =  form.lesson_cost.data
        lesson.lesson_description = form.lesson_description.data
        db.session.commit()
        flash('lesson Details Updated!')
        return lesson_details(id)

    elif request.method == "GET":
        form.lesson_name.data = lesson.lesson_name
        form.term.data = lesson.term
        form.day_of_class.data = lesson.day_of_class
        form.lesson_time.data = lesson.lesson_time
        form.lesson_duration.data = lesson.lesson_duration
        form.lesson_start_date.data = lesson.lesson_start_date
        form.lesson_cost.data = lesson.lesson_cost
        form.lesson_description.data = lesson.lesson_description
    return render_template('classes_pages/update_lesson.html',form=form) 


# show all lesson names with hyperlinks
@classes.route("/show_all_lessons")
@login_required
def show_all_lessons():
    lessons = Lesson.query.all()
    return render_template('classes_pages/show_all_lessons.html',lessons=lessons) 