from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo

states = [("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"), ("CA", "California"),
          ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"), ("FL", "Florida"), ("GA", "Georgia"),
          ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
          ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"),
          ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"),
          ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"), ("NH", "New Hampshire"),
          ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
          ("ND", "North Dakota"), ("OH", "Ohio"), ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"),
          ("RI", "Rhode Island"), ("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"),
          ("TX", "Texas"), ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"),
          ("WV", "West Virginia"), ("WI", "Wisconsin"), ("WY", "Wyoming")]

class InfoForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired(), Length(max=50)])
    address_1 = StringField("Address 1", validators=[DataRequired(), Length(max=100)])
    address_2 = StringField("Address 2", validators=[Length(max=100)])
    city = StringField("City", validators=[DataRequired(), Length(max=100)])
    state = SelectField("State", validators=[DataRequired()], choices=[_[0] for _ in states])
    zipcode = StringField("Zipcode", validators=[DataRequired(), Length(min=5, max=9)])
    submit = SubmitField("Save")

class QuoteFuelForm(FlaskForm):
    gallons_requested = IntegerField("Gallons Requested", validators=[DataRequired(), NumberRange(min=1)])
    delivery_address = StringField("Delivery Address", validators=[DataRequired()], render_kw={"readonly": True})
    delivery_date = DateField("Delivery Date", validators=[DataRequired()])
    suggested_price = IntegerField("Suggested Price / gallon", validators=[DataRequired()], render_kw={"readonly": True})
    total_amount_due = IntegerField("Total Amount Due", validators=[DataRequired()], render_kw={"readonly": True})
    submit = SubmitField("Submit")

class QuoteFuelHistory(FlaskForm):
    column_names = ['Timestamp',
                    'Gallons Requested',
                    'Delivery Address',
                    'Delivery Date',
                    'Suggested Price / gallon',
                    'Total Amount Due']
    # hard-coded the history data since we don't have a backend yet
    history_data = {}
    history_data['02/16/2023 5:10pm'] = [2, 'Center Street', '03/01/2023', '$3.00', '$6.00']
    history_data['02/17/2023 5:10pm'] = [2, 'Center Street', '03/01/2023', '$3.00', '$6.00']
    history_data['02/18/2023 5:10pm'] = [2, 'Center Street', '03/01/2023', '$3.00', '$6.00']

class UserForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), EqualTo("password_verified", message="Password Must Match!")])
    password_verified = PasswordField("Verify Password: ", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Login")