# people/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import User, Person, Child
from heart_hand.people.forms import CustomerEntryForm, ChildEntryForm
from datetime import datetime

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


# return customer details using their id
@people.route("/<int:id>")
@login_required
def customer_details(id):
    page = request.args.get('page',1,type=int)
    # return customer or 404 page (customer not found)
    customer = Person.query.filter_by(id=id).first_or_404()
    children = Child.query.filter_by(parent_id=id)
    return render_template('people_pages/customer_details.html',customer=customer, children=children)


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


# show all customer names with hyperlinks
@people.route("/show_all_customers")
@login_required
def show_all_customers():
    customers = Person.query.all()
    return render_template('people_pages/show_all_customers.html',customers=customers) 


# add child
@people.route("/add_child/<int:parent_id>",methods=['GET','POST'])
@login_required
def add_child(parent_id):
    
    form = ChildEntryForm()
    parent = Person.query.filter_by(id=parent_id).first_or_404()
    if request.method == 'POST':
        if form.validate():
            child = Child(parent_id=parent_id,first_name=request.form['first_name'],last_name=request.form['last_name'],date_of_birth=request.form['date_of_birth'],notes=request.form['notes'])
            form.populate_obj(child)
            db.session.add(child)
            db.session.commit()
            flash('New child was successfully added')
            return customer_details(parent_id) 
        else:
            flash("Your form contained errors")
            return redirect(url_for('people.add_child', parent_id=parent_id))
    
    return render_template('people_pages/add_child.html', form=form, parent=parent) 


# return child details using their id
@people.route("/child_details/<int:child_id>")
@login_required
def child_details(child_id):
    # return child or 404 page (child not found)
    child = Child.query.filter_by(id=child_id).first_or_404()
    return render_template('people_pages/child_details.html',child=child)


# Update Child Details
@people.route('/update_child/<int:id>', methods=['GET','POST'])
@login_required
def update_child(id):

    form = ChildEntryForm()
    child = Child.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():

        child.first_name =  form.first_name.data
        child.last_name = form.last_name.data
        dob = form.date_of_birth.data
        child.date_of_birth = datetime.combine(dob, datetime.min.time())
        child.notes = form.notes.data
        db.session.commit()
        flash('Child Details Updated!')
        return child_details(id)

    elif request.method == "GET":
        form.first_name.data = child.first_name
        form.last_name.data = child.last_name
        form.date_of_birth.data = child.date_of_birth
        form.notes.data = child.notes
    return render_template('people_pages/update_child.html',form=form)     