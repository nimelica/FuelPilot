from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    client_information = db.relationship('ClientInformation', backref='user_credentials')
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ClientInformation(db.Model):
    __tablename__ = 'client_information'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    address_1 = db.Column(db.String(100), nullable=False)
    address_2 = db.Column(db.String(100))
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(9), nullable=False)
    user_credentials_id = db.Column(db.Integer, db.ForeignKey('user_credentials.id'))

class FuelQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons_requested = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    suggested_price = db.Column(db.Float)
    total_amount_due = db.Column(db.Float)
    client_id = db.Column(db.Integer, db.ForeignKey('client_information.id'))
