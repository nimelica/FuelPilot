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
        return redirect(url_for('views.home'))
    return render_template('signup.html', form=form)


@views.route("/fuel_quote_form", methods=['GET', 'POST'])
def fuel_quote_form():
    form = QuoteFuelForm()
    if form.validate_on_submit():
        # Save the user information to database or perform other actions
        return redirect(url_for('views.home'))
    return render_template('fuel_quote_form.html', form=form)