from flask import Blueprint ,render_template,redirect,url_for,flash
from .forms import *

views = Blueprint("views",__name__)

@views.route("/", methods=['GET','POST'])
def home():
    form = LoginForm()
    title = 'Home'
    return render_template("home.html",form=form,title=title)

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

@views.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm()
    title = 'Register'
    if form.validate_on_submit():
        flash("Sucessfully created Account!",category="sucess")
        return  redirect(url_for('views.home'))
    return render_template('signup.html', form=form, title=title)

@views.route("/login",methods=["GET","POST"])
def login():
   form = LoginForm()
   title = 'Login'
   if form.validate_on_submit():
        #check whether username/password if they exist rout to home page else alert user invalid input and rerender the template
        if form.username.data == "user1" and form.password.data == "1234":
            flash("Login was Sucessful!.",category="sucess")
            return  redirect(url_for('views.home'))
        else:
            flash("Invalid Username or Password please try again.",category="error")
            return render_template('login.html', form=form, title=title)
   return render_template('login.html', form=form, title=title)

@views.route("/profile_management", methods=['GET', 'POST'])
def profile_management():
    form = InfoForm()
    title = 'Profile'
    if form.validate_on_submit():
        flash("Sucessfully registered Profile!",category="sucess")
        return  redirect(url_for('views.home'))
    return render_template('profile_management.html', form=form, title=title)
