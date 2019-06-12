# users/view.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from heart_hand import db
from heart_hand.models import User
from heart_hand.users.forms import RegistrationForm,LoginForm,UpdateUserForm

users = Blueprint('users', __name__)


# register
@users.route('/registerUser', methods=['GET','POST'])
def registerUser():

    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(email=form.email.data,
               username=form.username.data,
               password=form.password.data)

        db.session.add(user) 
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('users.login'))
    else:
        flash_errors(form)    

    return render_template('users/registerUser.html',form=form)
     

# login
@users.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')

        next = request.args.get('next')

        if next == None or not next[0]=='/':
            next = url_for('core.index')

        return redirect(next)    

    return render_template('users/login.html', form=form)     


# logout
@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('users/account.html',form=form)              

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')