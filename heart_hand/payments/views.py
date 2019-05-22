# payments/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import User, Person, Child
from heart_hand.people.forms import CustomerEntryForm, ChildEntryForm
from datetime import datetime

payments = Blueprint('payments', __name__)
