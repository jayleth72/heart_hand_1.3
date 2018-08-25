# models.py
from heart_hand import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True,index=True)
    username = db.Column(db.String(64), unique=True,index=True)
    password_hash = db.Column(db.String(128))
    # active = db.Column(db.Boolean())
    # confirmed_at = db.Column(db.DateTime())
    # roles = db.relationship('Role', secondary=roles_users,
    #                         backref=db.backref('users', lazy='dynamic'))
    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}" 


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(255), unique=True)
    street_address = db.Column(db.String(150))
    suburb = db.Column(db.String(50))
    state = db.Column(db.String(50))
    postcode = db.Column(db.Integer())
    phone = db.Column(db.String(50))
    alternative_contact = db.Column(db.String(100))
    alternative_contact_phone = db.Column(db.String(50))
    notes = db.Column(db.String(255))                            

    def __init__(self,first_name,last_name,email,street_address,suburb,state,postcode,phone,alternative_contact,alternative_contact_phone,notes):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email
        self.street_address = street_address
        self.suburb = suburb 
        self.state = state
        self.postcode = postcode
        self.phone = phone
        self.alternative_contact = alternative_contact
        self.alternative_contact_phone = alternative_contact_phone
        self.notes = notes

    def __repr__(self):
         return f"First Name: {self.first_name} -- Last Name: {self.last_name}"  
             

class Child(db.Model):
    __tablename__ = "child"

    person = db.relationship(Person)

    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer(), db.ForeignKey('person.id'), nullable=False)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80),nullable=False)
    date_of_birth = db.Column(db.DateTime(),nullable=False)
    notes= db.Column(db.String(255)) 
    

class Lesson(db.Model):
    __tablename__ = "lesson"

    id = db.Column(db.Integer(), primary_key=True)
    lesson_name = db.Column(db.String(80))
    day_of_class = db.Column(db.String(80))
    lesson_time = db.Column(db.DateTime())
    lesson_duration = db.Column(db.Integer())
    lesson_cost = db.Column(db.Float())
    lesson_description = db.Column(db.String(255)) 


class Business_Costs(db.Model):
    __tablename__ = "business_costs"

    id = db.Column(db.Integer(), primary_key=True)
    cost_value = db.Column(db.Float())
    cost_name = db.Column(db.String(80))
    cost_incurred_date = db.Column(db.DateTime(),nullable=False,default=datetime.utcnow)
    includes_gst = db.Column(db.Boolean())
    cost_description = db.Column(db.String(255)) 


class Payments(db.Model):
    __tablename__ = "payments"

    person = db.relationship(Person)
    lesson = db.relationship(Lesson)

    id = db.Column(db.Integer(), primary_key=True)
    payee_id = db.Column(db.Integer(), db.ForeignKey('person.id'),nullable=False)
    lesson_id = db.Column(db.Integer(), db.ForeignKey('lesson.id'),nullable=False)
    payment_value = db.Column(db.Float())
    payment_name = db.Column(db.String(80))
    payment_type = db.Column(db.String(80))
    payment_date = db.Column(db.DateTime(),nullable=False,default=datetime.utcnow)
    includes_gst = db.Column(db.Boolean())
    cost_description = db.Column(db.String(255)) 


class Class_List(db.Model):
    __tablename__ = "class_list"

    person = db.relationship(Person)
  
    id = db.Column(db.Integer(), primary_key=True)
    participant_id = db.Column(db.Integer(), db.ForeignKey('person.id'),nullable=False)
    lesson_id = db.Column(db.Integer(), db.ForeignKey('lesson.id'),nullable=False)


    
