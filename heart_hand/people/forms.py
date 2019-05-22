# people/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField


class CustomerEntryForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(message='First name is required')])
    last_name = StringField('Last Name', validators=[InputRequired(message='Last name is required')])
    email = StringField('Email',validators=[DataRequired(),Email()])
    street_address = StringField('Street Address', validators=[InputRequired(message='Street address is required')])
    suburb = StringField('Suburb', validators=[InputRequired(message='Suburb is required')])
    state = SelectField(u'State', choices=[('QLD', 'Queensland'), ('NT', 'Northern Territory'), ('WA', 'Western Australia'), ('NSW', 'New South Wales'), ('Vic', 'Victoria'), ('Tas', 'Tasmania'), ('SA', 'South Australia')])
    postcode = IntegerField('Postcode', validators=[InputRequired(message='Postcode is required')])
    phone = StringField('Phone', validators=[InputRequired(message='Phone No. is required')])
    alternative_contact = StringField('Alternative Contact')
    alternative_contact_phone = StringField('Alternative Contact Phone')
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Customer')


class ChildEntryForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(message='First name is required')])
    last_name = StringField('Last Name', validators=[InputRequired(message='Last name is required')])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired(message='Date of birth is required')])
    notes = TextAreaField('Notes')  
    submit = SubmitField('Add Child')      
