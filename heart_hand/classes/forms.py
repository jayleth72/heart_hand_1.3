# classes/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField


class LessonEntryForm(FlaskForm):
    lesson_name = StringField('Lesson Name', validators=[InputRequired(message='Lesson name is required')])
    day_of_class = SelectField(u'Day of Class', choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')])
    lesson_time = StringField('Lesson Start Time',  validators=[InputRequired(message='Lesson time is required')])
    lesson_duration= IntegerField('Lesson Duration',  validators=[InputRequired(message='Lesson duration is required')])
    lesson_start_date = DateField('Lesson Start Date', format='%Y-%m-%d', validators=[InputRequired(message='Start Date is required')])
    lesson_cost = FloatField('Lesson Cost',  validators=[InputRequired(message='Lesson cost is required')])
    lesson_description = TextAreaField('Lesson Description')
    submit = SubmitField('Add Lesson')
