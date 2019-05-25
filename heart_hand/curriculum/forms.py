# curriculum/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class SubjectEntryForm(FlaskForm):
    subject_name = StringField('Subject Name', validators=[InputRequired(message='Subject Name is required')])
    subject_description = TextAreaField('Subject Description')
    submit = SubmitField('Add Subject')


class CurriculumEntryForm(FlaskForm):
    curriculum_name = StringField('Curriculum Name', validators=[InputRequired(message='Curriculum Name is required')])
    curriculum_year_level =  IntegerField('Curriculum Year Level', validators=[InputRequired(message='Year Level is required')])
    curriculum_description = TextAreaField('Curriclum Description')
    submit = SubmitField('Add Curriculum')

def get_subjects():
    from heart_hand.models import Subjects
    return Subjects.query.with_entities(Subjects.id)

def get_pk(obj):
    return str(obj)    

class CurriculumItemEntryForm(FlaskForm):
    subject_id = QuerySelectField(u'Subjects',query_factory=get_subjects, get_pk=get_pk)
    term =  SelectField(u'Term', choices=[(1, 1), (2, 2), (3, 3), (4, 4)], validators=[InputRequired(message='Term is required')], coerce=int)
    topic = StringField('Topic', validators=[InputRequired(message='Topic is required')])
    learnt_skill = StringField('Learnt skill', validators=[InputRequired(message='Learnt Skill is required')])
    concepts = StringField('Concepts', validators=[InputRequired(message='Concepts is required')])
    activity = StringField('Activity', validators=[InputRequired(message='Activity is required')])
    resources = StringField('Resources', validators=[InputRequired(message='Resources is required')])
    sample_to_collect = StringField('Sample to Collect', validators=[InputRequired(message='Sample to Collect is required')])
    information_recorded = StringField('Information recorded', validators=[InputRequired(message='Information recorded is required')])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Curriculum Item')
