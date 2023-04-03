from flask import Blueprint ,render_template, session, flash, redirect, url_for, request
from .forms import *
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

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
    if request.method == 'POST':
        # Create a new fuel quote object and add it to the database
        new_fuel_quote = FuelQuote(gallons_requested=form.gallons_requested.data,
                                       delivery_address=form.delivery_address.data,
                                       delivery_date=form.delivery_date.data,
                                       suggested_price=form.suggested_price.data,
                                       total_amount_due=form.total_amount_due.data,
                                       client_id=session['user_id'])

        db.session.add(new_fuel_quote)
        db.session.commit()
        # Check that the user_credentials_id attribute was set correctly
        flash('Fuel Quote Submitted!')
        return redirect(url_for('views.home'))
    return render_template('fuel_quote_form.html', form=form, title=title)
    

@views.route("/fuel_quote_history", methods=['GET', 'POST'])
def fuel_quote_history():
    form = QuoteFuelHistory()
    title = 'Quote History'
    user_id = session.get('user_id')

    # THIS IS HOW WE GET THE DATA FROM DATABASE 
    fuel_quotes = FuelQuote.query.filter_by(client_id=user_id).all()
    '''
    # WE CAN CONVERT EACH OF THEM INTO LISTS SEPERATELY
    gallons_requested_list = [quote.gallons_requested for quote in fuel_quotes]
    delivery_address_list = [quote.delivery_address for quote in fuel_quotes]
    delivery_date_list = [quote.delivery_date.strftime("%Y-%m-%d") for quote in fuel_quotes]
    suggested_price_list = [quote.suggested_price for quote in fuel_quotes]
    total_amount_due_list = [quote.total_amount_due for quote in fuel_quotes]

    # EXAMPLE
    print(gallons_requested_list)
    print(delivery_address_list)

    # OR JUST GET IT AS AN OBJECT
    print(fuel_quotes)
    '''
    # IN HTML JINJA TEMPLATES WE CAN ACCESS THEM AS
    for fuel_quote in fuel_quotes: 
         print(fuel_quote.id, fuel_quote.gallons_requested, fuel_quote.delivery_address, fuel_quote.delivery_date, fuel_quote.suggested_price, fuel_quote.total_amount_due)

    return render_template('fuel_quote_history.html', form=form, title=title, fuel_quotes=fuel_quotes)

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
            print("here")
            return redirect(url_for('views.fuel_quote_form'))
        
        # If the username or password is incorrect, show an error message
        flash('Invalid username or password', 'error')
        
    # Render the login page with the login form
    return render_template('login.html', form=form, title=title)


@views.route("/profile_management", methods=['GET', 'POST'])
def profile_management():
    form = InfoForm()
    title = 'Profile'
    # if form.validate_on_submit():
    if request.method == 'POST':
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
        return redirect(url_for('views.home'))

    return render_template('profile_management.html', form=form, title=title)
