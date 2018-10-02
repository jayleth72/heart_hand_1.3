# people/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import User, Person
from heart_hand.people.forms import CustomerEntryForm

people = Blueprint('people', __name__)


# people_menu
@people.route('/people_menu')
@login_required
def people_menu():
    return render_template('people_pages/people_menu.html')


@people.route('/add_customer', methods=['GET','POST'])
@login_required
def add_customer():

    form = CustomerEntryForm()

    if request.method == 'POST':
        if form.validate():
            customer = Person(first_name=request.form['first_name'],last_name=request.form['last_name'],email=request.form['email'],street_address=request.form['street_address']
                       ,suburb=request.form['suburb'],state=request.form['state'],postcode=request.form['postcode'],phone=request.form['phone']
                       ,alternative_contact=request.form['alternative_contact'],alternative_contact_phone=request.form['alternative_contact_phone'],notes=request.form['notes'])
            form.populate_obj(customer)
            
            db.session.add(customer)
            db.session.commit()
            flash('New customer was successfully added')
            # return redirect(url_for('add_child', arg1=request.form['first_name'],arg2=request.form['last_name'], arg3=request.form['email']))
            return customer_details(customer.email)
        else:
            flash("Your form contained errors")
            return redirect(url_for('people.add_customer'))
     
    return render_template('people_pages/add_customer.html', form=form)  


# @people.route('/customer_details', methods=['GET','POST'])
# @login_required
# def customer_details():

#     form = CustomerEntryForm()

#     if request.method == 'POST':
#         if form.validate():
#             customer = Person(first_name=request.form['first_name'],last_name=request.form['last_name'],email=request.form['email'],street_address=request.form['street_address']
#                        ,suburb=request.form['suburb'],state=request.form['state'],postcode=request.form['postcode'],phone=request.form['phone']
#                        ,alternative_contact=request.form['alternative_contact'],alternative_contact_phone=request.form['alternative_contact_phone'],notes=request.form['notes'])
#             form.populate_obj(customer)
            
#             db.session.add(customer)
#             db.session.commit()
#             flash('New customer was successfully Updated')
#             return redirect(url_for('customer_details'))
#         else:
#             flash("Your form contained errors")
#             return redirect(url_for('customer_details'))
     
#     return render_template('people_pages/customer_details.html', form=form)  

# return customer details using their email
@people.route("/<email>")
@login_required
def customer_details(email):
    page = request.args.get('page',1,type=int)
    # return customer or 404 page (customer not found)
    customer = Person.query.filter_by(email=email).first_or_404()
    return render_template('people_pages/customer_details.html',customer=customer)