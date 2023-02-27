from flask import Flask
from os import path, urandom
from .config import db

def create_app():
    app = Flask(__name__)

    # Set up secret key
    secret_key_file = path.join(app.instance_path, 'secret_key')
    if not path.exists(secret_key_file):
        # Generate a new secret key if one doesn't exist
        with open(secret_key_file, 'wb') as f:
            f.write(urandom(32))
    with open(secret_key_file, 'rb') as f:
        app.config['SECRET_KEY'] = f.read()

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize the database
    db.init_app(app)

    #import the modules
    from .views import views
    app.register_blueprint(views, url_prefix = "/")

    # import the models
    from .models import UserCredentials, ClientInformation

    return app

