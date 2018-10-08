# questionaire/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField
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