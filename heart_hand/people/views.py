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
            return customer_details(customer.id)
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
@people.route("/<int:id>")
@login_required
def customer_details(id):
    page = request.args.get('page',1,type=int)
    # return customer or 404 page (customer not found)
    customer = Person.query.filter_by(id=id).first_or_404()
    return render_template('people_pages/customer_details.html',customer=customer)


# Update Customer Details
@people.route('/update_customer/<int:id>', methods=['GET','POST'])
@login_required
def update_customer(id):

    form = CustomerEntryForm()
    customer = Person.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():

        customer.first_name =  form.first_name.data
        customer.last_name = form.last_name.data 
        customer.email = form.email.data 
        customer.street_address = form.street_address.data
        customer.suburb = form.suburb.data
        customer.state =  form.state.data
        customer.postcode = form.postcode.data
        customer.phone = form.phone.data
        customer.alternative_contact = form.alternative_contact.data
        customer.alternative_contact_phone = form.alternative_contact_phone.data
        customer.notes = form.notes.data
        db.session.commit()
        flash('Customer Details Updated!')
        return customer_details(id)

    elif request.method == "GET":
        form.first_name.data = customer.first_name
        form.last_name.data = customer.last_name
        form.email.data = customer.email
        form.street_address.data = customer.street_address
        form.suburb.data = customer.suburb
        form.state.data = customer.state
        form.postcode.data = customer.postcode
        form.phone.data = customer.phone
        form.alternative_contact.data = customer.alternative_contact
        form.alternative_contact_phone.data = customer.alternative_contact_phone
        form.notes.data = customer.notes
    return render_template('people_pages/update_customer.html',form=form) 