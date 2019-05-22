# curriculum/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField


class SubjectEntryForm(FlaskForm):
    subject_name = StringField('Subject Name', validators=[InputRequired(message='Subject Name is required')])
    subject_description = TextAreaField('Subject Description')
    submit = SubmitField('Add Subject')


class CurriculumEntryForm(FlaskForm):
    year_level =  IntegerField('Year Level', validators=[InputRequired(message='Year Level is required')])
    term =  IntegerField('Term', validators=[InputRequired(message='Term is required')])
    topic = StringField('Topic', validators=[InputRequired(message='Topic is required')])
    learnt_skill = StringField('Learnt skill', validators=[InputRequired(message='Learnt Skill is required')])
    concepts = StringField('Concepts', validators=[InputRequired(message='Concepts is required')])
    activity = StringField('Activity', validators=[InputRequired(message='Activity is required')])
    resources = StringField('Resources', validators=[InputRequired(message='Resources is required')])
    sample_to_collect = StringField('Sample to Collect', validators=[InputRequired(message='Sample to Collect is required')])
    information_recorded = StringField('Information recorded', validators=[InputRequired(message='Information recorded is required')])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Curriculum Item')
    