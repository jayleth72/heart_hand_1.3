# payments/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import User, Person
from heart_hand.payments.forms import PaymentsEntryForm
from datetime import datetime

payments = Blueprint('payments', __name__)


# # add payment
# @payments.route("/add_payment/<int:person_id>",methods=['GET','POST'])
# @login_required
# def add_payment(person_id):
    
#     form = PaymentEntryForm()
#     person = Person.query.filter_by(id=person_id).first_or_404()
    
#     if request.method == 'POST':
#         if form.validate():
#             payment = Payment(person_id=person_id,first_name=request.form['first_name'],last_name=request.form['last_name'],date_of_birth=request.form['date_of_birth'],notes=request.form['notes'])
#             form.populate_obj(child)
#             db.session.add(child)
#             db.session.commit()
#             flash('New child was successfully added')
#             return customer_details(parent_id) 
#         else:
#             flash("Your form contained errors")
#             return redirect(url_for('people.add_child', parent_id=parent_id))
    
#     return render_template('people_pages/add_child.html', form=form, parent=parent) 