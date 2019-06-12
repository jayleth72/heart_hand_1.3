# curriculum/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_table import Table, Col

class SubjectEntryForm(FlaskForm):
    subject_name = StringField('Subject Name', validators=[InputRequired(message='Subject Name is required')])
    subject_description = TextAreaField('Subject Description')
    submit = SubmitField('Add Subject')

def get_subjects():
    from heart_hand.models import Subjects
    return Subjects.query.with_entities(Subjects.subject_name)

def get_pk(obj):
    return str(obj)


class CurriculumEntryForm(FlaskForm):
    curriculum_name = StringField('Curriculum Name', validators=[InputRequired(message='Curriculum Name is required')])
    curriculum_year_level =  IntegerField('Curriculum Year Level', validators=[InputRequired(message='Year Level is required')])
    curriculum_description = TextAreaField('Curriclum Description')
    submit = SubmitField('Add Curriculum')
  

class CurriculumItemEntryForm(FlaskForm):
    subject = QuerySelectField(u'Subjects',query_factory=get_subjects, get_pk=get_pk, get_label='subject_name', allow_blank=True)
    term =  SelectField(u'Term', choices=[(1, 1), (2, 2), (3, 3), (4, 4)], validators=[InputRequired(message='Term is required')], coerce=int)
    topic = StringField('Topic', validators=[InputRequired(message='Topic is required')])
    learnt_skill = TextAreaField('Learnt skill', validators=[InputRequired(message='Learnt Skill is required')])
    concepts = TextAreaField('Concepts')
    activity = TextAreaField('Activity', validators=[InputRequired(message='Activity is required')])
    resources = TextAreaField('Resources', validators=[InputRequired(message='Resources is required')])
    sample_to_collect = TextAreaField('Sample to Collect', validators=[InputRequired(message='Sample to Collect is required')])
    information_recorded = TextAreaField('Information recorded', validators=[InputRequired(message='Information recorded is required')])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Curriculum Item')


class SubjectTermSelectorForm(FlaskForm):
    subject = QuerySelectField(u'Subjects',query_factory=get_subjects, get_pk=get_pk, get_label='subject_name', allow_blank=True)
    term =  SelectField(u'Term', choices=[(1, 1), (2, 2), (3, 3), (4, 4)], validators=[InputRequired(message='Term is required')], coerce=int)
    submit = SubmitField('Select Term & Subject')


class CurriculumItemsTable(Table):
    id = Col('Id', show=False)
    curriculum_id = Col('Curriculum Id', show=False)
    subject = Col('Subject', show=False)
    term = Col('Term', show=False)
    topic = Col('Topic')
    learnt_skill = Col('Learnt Skills')
    concepts = Col('Concepts')
    activity = Col('Activity')
    resources = Col('Resources')
    sample_to_collect = Col('Sample to Collect')
    information_recorded = Col('Information recorded')
    notes = Col('Notes', show=False)  
