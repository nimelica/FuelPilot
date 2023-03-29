from flask import Blueprint ,render_template, session, flash, redirect, url_for
from .forms import *
from .models import *

views = Blueprint("views",__name__)

@views.route("/", methods=['GET','POST'])
def home():
    form = LoginForm()
    title = 'Home'
    return render_template("home.html",form=form,title=title)

@views.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm()
    title = 'Register'
    if form.validate_on_submit():
        # Check if the username already exists in the database
        existing_user = UserCredentials.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('views.signup'))

        # Create a new UserCredentials object and add it to the database
        new_user = UserCredentials(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        # Set the user's ID as a session variable so they are logged in
        session['user_id'] = new_user.id

        flash('Account created successfully')
        return redirect(url_for('views.home'))

    return render_template('signup.html', form=form, title=title)


@views.route("/fuel_quote_form", methods=['GET', 'POST'])
def fuel_quote_form():
    form = QuoteFuelForm()
    title = 'Quote Form'
    return render_template('fuel_quote_form.html', form=form, title=title)


@views.route("/fuel_quote_history", methods=['GET', 'POST'])
def fuel_quote_history():
    form = QuoteFuelHistory()
    title = 'Quote History'
    return render_template('fuel_quote_history.html', form=form, title=title)


@views.route("/login",methods=["GET","POST"])
def login():
   form = LoginForm()
   title = 'Login'
   #check submission and if login is in database
   if form.validate_on_submit():
        #return redirect(url_for('views.home'))
        return None
   # todo: check user exist in db
   # if yes, let signin -> create or go to user page
   return render_template('login.html', form=form, title=title)


@views.route("/profile_management", methods=['GET', 'POST'])
def profile_management():
    form = InfoForm()
    title = 'Profile'
    return render_template('profile_management.html', form=form, title=title)
