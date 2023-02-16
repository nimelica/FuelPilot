from flask import Blueprint ,render_template
from .forms import *

views = Blueprint("views",__name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm()
    title = 'Register'
    if form.validate_on_submit():
        # Save the user information to database or perform other actions
        #return redirect(url_for('views.home'))
        return None
    return render_template('signup.html', form=form, title=title)


@views.route("/fuel_quote_form", methods=['GET', 'POST'])
def fuel_quote_form():
    form = QuoteFuelForm()
    title = 'Quote Form'
    return render_template('fuel_quote_form.html', form=form, title=title)


@views.route("/login",methods=["GET","POST"])
def login():
   form = LoginForm()
   title = 'Login'
   #check submission and if login is in database
   if form.validate_on_submit():
        #return redirect(url_for('views.home'))
        return None
   return render_template('login.html', form=form, title=title)


@views.route("/profile_management", methods=['GET', 'POST'])
def profile_management():
    form = InfoForm()
    title = 'Profile'
    return render_template('profile_management.html', form=form, title=title)
