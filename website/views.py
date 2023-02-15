from flask import Blueprint ,render_template
from .forms import *

views = Blueprint("views",__name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        # Save the user information to database or perform other actions
        #return redirect(url_for('views.home'))
        return None
    return render_template('signup.html', form=form)


@views.route("/fuel_quote_form", methods=['GET', 'POST'])
def fuel_quote_form():
    form = QuoteFuelForm()
    return render_template('fuel_quote_form.html', form=form)


@views.route("/login",methods=["GET","POST"])
def login():
   form = LoginForm()
   #check submission and if login is in database
   if form.validate_on_submit():
        #return redirect(url_for('views.home'))
        return None
   return render_template('login.html', form=form)


@views.route("/profile_management", methods=['GET', 'POST'])
def profile_management():
    form = InfoForm()
    return render_template('profile_management.html', form=form)
