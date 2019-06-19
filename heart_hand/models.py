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
        # self.roles = roles

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
    term = db.Column(db.Integer())
    day_of_class = db.Column(db.String(80))
    lesson_time = db.Column(db.String(80))
    lesson_duration = db.Column(db.Integer())
    lesson_start_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    lesson_cost = db.Column(db.Float())
    lesson_description = db.Column(db.String(255))

    def __init__(self, lesson_name, term, day_of_class, lesson_time, lesson_duration, lesson_start_date, lesson_cost, lesson_description):
        self.lesson_name = lesson_name
        self.term = term
        self.day_of_class = day_of_class
        self.lesson_time = lesson_time
        self.lesson_duration = lesson_duration
        self.lesson_cost = lesson_cost
        self.lesson_start_date = lesson_start_date
        self.lesson_cost = db.Column(db.Float())
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
    lesson_id = db.Column(db.Integer(), db.ForeignKey('lesson.id'), nullable=False)
    program_name = db.Column(db.String(80))
    program_cost = db.Column(db.Float())
    program_discount = db.Column(db.Float())
    program_description = db.Column(db.String(255))

    def __init__(self, program_name, lesson_id, program_cost, program_discount, program_description):
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
    class_program = db.relationship(Class_Program)

    id = db.Column(db.Integer(), primary_key=True)
    payee_id = db.Column(db.Integer(), db.ForeignKey('person.id'), nullable=False)
    lesson_id = db.Column(db.Integer(), db.ForeignKey('lesson.id'), nullable=True)
    class_program_id = db.Column(db.Integer(), db.ForeignKey('class_program.id'), nullable=True)
    payment_value = db.Column(db.Float())
    payment_name = db.Column(db.String(80))
    payment_type = db.Column(db.String(80))
    payment_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    includes_gst = db.Column(db.Boolean())
    payment_description = db.Column(db.String(255))

    def __init__(self, payee_id, lesson_id, class_program_id, payment_value, payment_name, payment_type, payment_date, includes_gst, payment_description):
        self.payee_id = payee_id
        self.lesson_id = lesson_id
        self.class_program_id = class_program_id
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

    def __init__(self, questionaire_name, questionaire_type, description):
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

    def __init__(self, questionaire_id, question,response):
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


######################################
######### CURRICULUM MODELS ############
######################################
class Subjects(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer(), primary_key=True)
    subject_name = db.Column(db.String(80))
    subject_description = db.Column(db.String(255)) 

    def __init__(self,subject_name,subject_description):
        self.subject_name = subject_name
        self.subject_description = subject_description

    def __repr__(self):
         return  {self.id}

    def subject_choice_query():
        return Subjects.query

    def __str__(self):
        return str(self.subject_name)

class Curriculum(db.Model):
    __tablename__ = "curriculum"

    id = db.Column(db.Integer(), primary_key=True)
    curriculum_name = db.Column(db.String(80))
    curriculum_year_level = db.Column(db.Integer())
    curriculum_description = db.Column(db.String(255)) 

    def __init__(self,curriculum_name,curriculum_year_level,curriculum_description):
        self.curriculum_name = curriculum_name
        self.curriculum_year_level = curriculum_year_level
        self.curriculum_description = curriculum_description

    def __repr__(self):
         return f"Curriculum: {self.curriculum_name} -- Curriculum Description: {self.curriculum_description}"


class Curriculum_Item(db.Model):
    __tablename__ = "curriculum_item"
    
    Curriculum = db.relationship(Curriculum)
    
    id = db.Column(db.Integer(), primary_key=True)
    curriculum_id = db.Column(db.Integer(), db.ForeignKey('curriculum.id'),nullable=False)
    subject = db.Column(db.String(80))
    term = db.Column(db.Integer())
    topic = db.Column(db.String(400))
    learnt_skill = db.Column(db.String(400))
    concepts = db.Column(db.String(400))
    activity = db.Column(db.String(400))
    resources = db.Column(db.String(400))
    sample_to_collect = db.Column(db.String(400))
    information_recorded = db.Column(db.String(400))
    notes = db.Column(db.String(400)) 
   
    def __init__(self,curriculum_id,subject,term,topic,learnt_skill,concepts,activity,resources,sample_to_colect,information_recorded,notes):
        self.curriculum_id = curriculum_id
        self.subject= subject
        self.term = term
        self.topic = topic
        self.learnt_skill = learnt_skill
        self.concepts = concepts
        self.activity = activity
        self.resources = resources
        self.sample_to_collect = sample_to_colect
        self.information_recorded = information_recorded
        self.notes = notes

    def __repr__(self):
         return f"Curriculum Item: {self.id}"         
######################################