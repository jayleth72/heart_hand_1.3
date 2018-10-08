# questionaire/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import Questionaire
from heart_hand.questionaire.forms import QuestionaireForm
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
@questionaire.route("/questionaire_details/<int:id>")
@login_required
def questionaire_details(id):
    # return questionaire or 404 page (questioniare not found)
    questionaire = Questionaire.query.filter_by(id=id).first_or_404()
    return render_template('questionaire_pages/questionaire_type_details.html',questionaire=questionaire)

# show all questionaire types with hyperlinks
@questionaire.route("/show_all_questionaire_types")
@login_required
def show_all_questionaire_types():
    questionaires = Questionaire.query.all()
    return render_template('questionaire_pages/show_all_questionaire_types.html',questionaires=questionaires) 
    