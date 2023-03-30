from flask import Blueprint ,render_template, session, flash, redirect, url_for
from .forms import *
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint("views",__name__)

@views.route("/", methods=['GET','POST'])
def home():
    form = LoginForm()
    title = 'Home'
    if 'user_id' in session:
        return render_template('home.html',form=form,title=title)
    else:
        return redirect(url_for('views.login'))
    return render_template("home.html",form=form,title=title)

@views.route("/signout", methods=['GET', 'POST'])
def signout():
    session.clear()
    form = LoginForm()
    title = 'Home'
    flash('You have sucessfully logged out!')
    return render_template('home.html',form=form,title=title)

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

        #Set the user's ID as a session variable so they are logged in
        session['user_id'] = new_user.id

        flash('Account created successfully')
        return redirect(url_for('views.profile_management'))

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


# TODO: add user-profile dashboard page
@views.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    title = 'Login'
    # check submission and if login is in database
    if form.validate_on_submit():
        # Get the username and password from the form
        username = form.username.data
        password = form.password.data
        
        # Check if the username exists in the database
        user = UserCredentials.query.filter_by(username=username).first()

        # If the username exists, check if the password is correct
        if user and user.check_password(password):
            # If the password is correct, log the user in and redirect them to the home page
            session['user_id'] = user.id
            return redirect(url_for('views.home'))
        
        # If the username or password is incorrect, show an error message
        flash('Invalid username or password', 'error')
        
    # Render the login page with the login form
    return render_template('login.html', form=form, title=title)


@views.route("/profile_management", methods=['GET', 'POST'])
def profile_management():
    form = InfoForm()
    title = 'Profile'
    if form.validate_on_submit():
        # Create a new ClientInformation object and add it to the database
        new_client = ClientInformation(full_name=form.full_name.data,
                                       address_1=form.address_1.data,
                                       address_2=form.address_2.data,
                                       city=form.city.data,
                                       state=form.state.data,
                                       zipcode=form.zipcode.data,
                                       user_credentials_id=session['user_id'])
        db.session.add(new_client)
        db.session.commit()

        # Check that the user_credentials_id attribute was set correctly
        print(new_client.user_credentials_id)

        flash('Profile information saved successfully')
        return redirect(url_for('views.login'))
    return render_template('profile_management.html', form=form, title=title)



