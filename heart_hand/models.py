# models.py
from heart_hand import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_security import RoleMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

######################################
######### USER MODELS ################
######################################
class User(db.Model, UserMixin):
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
        self.roles = roles

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}" 
######################################


######################################
######### PEOPLE MODELS ##############
######################################
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
    notes = db.Column(db.String(255)) 
    
    def __init__(self,parent_id,first_name,last_name,date_of_birth,notes):
        self.parent_id = parent_id 
        self.first_name = first_name 
        self.last_name = last_name 
        self.date_of_birth = date_of_birth
        self.notes = notes

    def __repr__(self):
        return f"First Name: {self.first_name} -- Last Name: {self.last_name}" 
######################################


######################################
######### CLASS MODELS ##############
######################################
class Lesson(db.Model):
    __tablename__ = "lesson"

    id = db.Column(db.Integer(), primary_key=True)
    lesson_name = db.Column(db.String(80))
    day_of_class = db.Column(db.String(80))
    lesson_time = db.Column(db.DateTime())
    lesson_duration = db.Column(db.Integer())
    lesson_recurring = db.Column(db.Boolean())
    lesson_recurring_period = db.Column(db.String(80))
    lesson_cost = db.Column(db.Float())
    lesson_description = db.Column(db.String(255)) 

    def __init__(self,lesson_name,day_of_class,lesson_time,lesson_duration,lesson_cost,lesson_recurring,lesson_recurring_period,lesson_description):
        self.lesson_name= lesson_name
        self.day_of_class= day_of_class 
        self.lesson_time= lesson_time
        self.lesson_duration = lesson_duration
        self.lesson_cost = lesson_cost
        self.lesson_recurring = lesson_recurring
        self.lesson_recurring_period = lesson_recurring_period
        self.lesson_description = lesson_description

    def __repr__(self):
         return f"Lesson: {self.lesson_name}" 


class Class_List(db.Model):
    __tablename__ = "class_list"

    person = db.relationship(Person)
  
    id = db.Column(db.Integer(), primary_key=True)
    participant_id = db.Column(db.Integer(), db.ForeignKey('person.id'),nullable=False)
    lesson_id = db.Column(db.Integer(), db.ForeignKey('lesson.id'),nullable=False)

    def __init__(self,participant_id,lesson_id):
        self.participant_id= participant_id 
        self.lesson_id = lesson_id
       
    def __repr__(self):
         return f"Lesson Id: {self.lesson_id} -- Participant Id: {self.participant_id}"


class Class_Program(db.Model):
    __tablename__ = "class_program"

    lesson = db.relationship(Lesson)
  
    id = db.Column(db.Integer(), primary_key=True)
    lesson_id = db.Column(db.Integer(), db.ForeignKey('lesson.id'),nullable=False)
    program_name = db.Column(db.String(80))
    program_cost = db.Column(db.Float())
    program_discount = db.Column(db.Float())
    program_description = db.Column(db.String(255))

    def __init__(self,program_name,lesson_id,program_cost,program_discount,program_description):
        self.program_name = program_name
        self.lesson_id = lesson_id
        self.program_cost = program_cost
        self.program_discount = program_discount
        self.program_description = program_description

    def __repr__(self):
         return f"Program Name {self.program_name}"         
######################################


######################################
######### BUSINESS COST MODELS #######
######################################
class Business_Costs(db.Model):
    __tablename__ = "business_costs"

    id = db.Column(db.Integer(), primary_key=True)
    cost_value = db.Column(db.Float())
    cost_name = db.Column(db.String(80))
    cost_incurred_date = db.Column(db.DateTime(),nullable=False,default=datetime.utcnow)
    includes_gst = db.Column(db.Boolean())
    cost_description = db.Column(db.String(255)) 

    def __init__(self,cost_value,cost_name,cost_incurred_date ,includes_gst,cost_description):
        self.cost_value = cost_value
        self.cost_name = cost_value
        self.cost_incurred_date = cost_incurred_date
        self.includes_gst = includes_gst
        self.cost_description = cost_description

    def __repr__(self):
         return f"Type of cost: {self.cost_name} -- Cost Value: {self.cost_value}"
######################################


######################################
######### PAYMENTS MODELS ############
######################################
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
    payment_description = db.Column(db.String(255)) 

    def __init__(self,payee_id,lesson_id,payment_value,payment_name,payment_type,payment_date,includes_gst,payment_description):
        self.payee_id = payee_id 
        self.lesson_id = lesson_id
        self.payment_value = payment_value
        self.payment_name = payment_name
        self.payment_type = payment_type
        self.payment_date = payment_date
        self.includes_gst = includes_gst
        self.payment_description = payment_description

    def __repr__(self):
        return f"Payment Name: {self.payment_name} -- Payment Value: {self.payment_value} -- Payment Date: {self.payment_date}" 
######################################


######################################
######### QUESTIONAIRE MODELS ########
######################################
class Questionaire(db.Model):
    __tablename__ = "questionaire"

    id = db.Column(db.Integer(), primary_key=True)
    questionaire_name = db.Column(db.String(80))
    questionaire_type = db.Column(db.String(50))
    description = db.Column(db.String(255))

    def __init__(self,questionaire_name,questionaire_type,description):
        self.questionaire_name = questionaire_name
        self.questionaire_type = questionaire_type
        self.description = description

    def __repr__(self):
         return f"Questionaire Name {self.questionaire_name}"


class Questionaire_Questions(db.Model):
    __tablename__ = "questionaire_questions"

    questionaire = db.relationship(Questionaire)

    id = db.Column(db.Integer(), primary_key=True)
    questionaire_id = db.Column(db.Integer(), db.ForeignKey('questionaire.id'),nullable=False)
    question = db.Column(db.String(120))
    response = db.Column(db.String(50))

    def __init__(self,questionaire_id,question,response):
        self.questionaire_id = questionaire_id
        self.question = question
        self.response = response

    def __repr__(self):
         return f"Questionaire Questions {self.question}"


class Child_Questionaire_Questions(db.Model):
    __tablename__ = "child_questionaire_questions"

    questionaire_questions = db.relationship(Questionaire_Questions)
    child = db.relationship(Child)

    id = db.Column(db.Integer(), primary_key=True)
    question_id = db.Column(db.Integer(), db.ForeignKey('questionaire_questions.id'),nullable=False)
    child_id = db.Column(db.Integer(), db.ForeignKey('child.id'),nullable=False)
    
    def __init__(self,question_id,child_id):
        self.question_id = question_id
        self.child_id = child_id

    def __repr__(self):
         return f"Child Questions {self.id}" 


class Customer_Questionaire_Questions(db.Model):
    __tablename__ = "customer_questionaire_questions"

    questionaire_questions = db.relationship(Questionaire_Questions)
    person = db.relationship(Person)

    id = db.Column(db.Integer(), primary_key=True)
    question_id = db.Column(db.Integer(), db.ForeignKey('questionaire_questions.id'),nullable=False)
    customer_id = db.Column(db.Integer(), db.ForeignKey('person.id'),nullable=False)
    
    def __init__(self,question_id,customer_id):
        self.question_id = question_id
        self.customer_id = customer_id

    def __repr__(self):
         return f"Customer Questions {self.id}"
######################################