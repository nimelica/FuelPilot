from website.models import db
from website.models import UserCredentials, ClientInformation, FuelQuote

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

