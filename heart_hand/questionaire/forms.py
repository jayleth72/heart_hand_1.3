# questionaire/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField


class QuestionaireForm(FlaskForm):
    questionaire_name = StringField('Questionaire Name', validators=[InputRequired(message='name is required')])
    questionaire_type = SelectField(u'Questionaire Type', choices=[('Medical', 'Medical'), ('Feedback', 'Feedback')])
    description = TextAreaField('Notes')  
    submit = SubmitField('Add New Questionaire') 

class QuestionaireQuestionForm(FlaskForm):
    question = StringField('Question', validators=[InputRequired(message='Question is required')])
    response = SelectField(u'Questionaire Type', choices=[('Yes', 'Yes'), ('No', 'No'), ('None', 'None')])
    submit = SubmitField('Submit Question') 

class QuestionaireYesNoQuestionForm(FlaskForm):
    question = StringField('Question', validators=[InputRequired(message='Question is required')])
    response = SelectField(u'Questionaire Type', choices=[('Yes', 'Yes'), ('No', 'No'), ('None', 'None')])

class QuestionaireGroupForm(FlaskForm):
    title = StringField('Title')
    grouped_questions = FieldList(FormField(QuestionaireYesNoQuestionForm)) 
       
        