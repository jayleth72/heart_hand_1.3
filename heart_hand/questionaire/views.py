# questionaire/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import Questionaire, Questionaire_Questions
from heart_hand.questionaire.forms import QuestionaireForm, QuestionaireQuestionForm, QuestionaireYesNoQuestionForm, QuestionaireGroupForm
from datetime import datetime

questionaire = Blueprint('questionaire', __name__)


# add questionaire type
@questionaire.route("/add_questionaire_type",methods=['GET','POST'])
@login_required
def add_questionaire_type():
    
    form = QuestionaireForm()
    
    if request.method == 'POST':
        if form.validate():
            questionaire = Questionaire(questionaire_name=request.form['questionaire_name'],questionaire_type=request.form['questionaire_type'],description=request.form['description'])
            form.populate_obj(questionaire)
            db.session.add(questionaire)
            db.session.commit()
            flash('New Questionaire was successfully added')
            return questionaire_details(questionaire.id) 
        else:
            flash("Your form contained errors")
            return redirect(url_for('questionaire.add_questionaire_type'))
    
    return render_template('questionaire_pages/add_questionaire_type.html', form=form) 


# return customer details using their id
@questionaire.route("/questionaire_details/<int:id>", methods=['GET','POST'])
@login_required
def questionaire_details(id):

    questionaireform = QuestionaireGroupForm()
    questionaireform.title.data = "My Questionaire"
    # return questionaire or 404 page (questioniare not found)
    questionaire = Questionaire.query.filter_by(id=id).first_or_404()
    # retrieve questions for this questionaire type
    # questions = show_all_questions(id)
    questions = show_all_questions(id)
    # if questionaireform .validate_on_submit():
    #     for question in questions:
    #         question_form = QuestionaireYesNoQuestionForm()
    #         question.question = question_form.question
    #         question.response = question_form.response
            
    #     db.sesssion.commit()
    #     questionaires = Questionaire.query.all()
    #     return render_template('questionaire_pages/show_all_questionaire_types.html',questionaires=questionaires)    
    # elif request.method == "GET":
    for question in questions:
        question_form = QuestionaireYesNoQuestionForm()
        question_form.question = question.question
        question_form.response = question.response

        questionaireform.grouped_questions.append_entry(question_form)

    # return render_template('questionaire_pages/questionaire_type_details.html',questionaire=questionaire,questions=questions)
    return render_template('questionaire_pages/edit-questionaire.html', form=questionaireform)

# show all questionaire types with hyperlinks
@questionaire.route("/show_all_questionaire_types")
@login_required
def show_all_questionaire_types():
    questionaires = Questionaire.query.all()
    return render_template('questionaire_pages/show_all_questionaire_types.html',questionaires=questionaires) 

# add question
@questionaire.route("/add_question/<int:questionaire_id>",methods=['GET','POST'])
@login_required
def add_question(questionaire_id):
    
    form = QuestionaireQuestionForm()
    
    if request.method == 'POST':
        if form.validate():
            question = Questionaire_Questions(questionaire_id=questionaire_id,question=request.form['question'],response=request.form['response'])
            form.populate_obj(question)
            db.session.add(question)
            db.session.commit()
            flash('New Questiona was successfully added')
            return questionaire_details(questionaire_id) 
        else:
            flash("Your form contained errors")
            return redirect(url_for('questionaire.add_question'))
    
    return render_template('questionaire_pages/add_question.html', form=form) 


# show all questions for a questionaire type
@questionaire.route("/show_all_questions/<int:questionaire_id>")
@login_required
def show_all_questions(questionaire_id):
    questions = Questionaire_Questions.query.filter_by(questionaire_id=questionaire_id)
    return questions

# update questions for a questionaire type
@questionaire.route("/update_all_questions", methods=['GET', 'POST'])
@login_required
def update_all_questions(questionaire_id):
    questionaireform = QuestionaireGroupForm()
    questionaireform.title.data = "My Questionaire"

    for question in db.get('grouped_questions'):
        question_form = QuestionaireYesNoQuestionForm()
        question_form.question = question.question
        question_form.response = question.response

        questionaireform.grouped_questions.append_entry(question_form)

   
    return render_template('edit-questionaire.html', questionaireform=questionaireform)