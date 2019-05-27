# payments/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField, DateField


class PaymentsEntryForm(FlaskForm):
    payment_value = FloatField('Payment Value', validators=[InputRequired(message='Payment value is required')])
    payment_name = StringField('Payment Name', validators=[InputRequired(message='Payment name is required')])
    payment_type = SelectField(u'Payment Type', choices=[('cash', 'cash'), ('bank transfer', 'bank transfer'), ('paypal', 'paypal')])
    payment_date = DateField('Payment Date', format='%Y-%m-%d', validators=[InputRequired(message='Payment Date is required')])
    includes_gst = SelectField(u'Includes GST', choices=[('No', 'No'), ('Yes', 'Yes')])
    payment_description = TextAreaField('Payment Description')
    submit = SubmitField('Add Payment')

    