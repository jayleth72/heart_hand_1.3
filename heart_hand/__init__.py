# heart_heart/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from heart_hand.settings import *
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

######################################
######### DATABASE SETUP #############
######################################
app.config['SQLALCHEMY_DATABASE_URI']= DATABASE_URI
app.config['SECRET_KEY']= SECRET_KEY 
app.config['SECURITY_REGISTERABLE']= SECURITY_REGISTERABLE
app.config['SECURITY_PASSWORD_HASH'] = SECURITY_PASSWORD_HASH 
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT 

db = SQLAlchemy(app)
Migrate(app,db)
######################################

######################################
######### LOGIN CONFIGS #############
######################################
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

######################################


######################################
######### BLUEPRINT REGISTER #########
######################################
from heart_hand.core.views import core
from heart_hand.users.views import users
from heart_hand.people.views import people
from heart_hand.questionaire.views import questionaire
from heart_hand.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(people)
app.register_blueprint(questionaire)
app.register_blueprint(error_pages)


######################################
############# FLASK SECURITY ############
######################################
from flask_security import Security, SQLAlchemyUserDatastore
from heart_hand.models import *

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

######################################


######################################
############# ADMIN PANEL ############
######################################
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Child, db.session))

######################################