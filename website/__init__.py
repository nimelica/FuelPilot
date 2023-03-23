from .db_init import init_db
from flask import Flask
from os import path, urandom

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

    # Configuring SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    init_db(app)

    #import the modules
    from .views import views

    app.register_blueprint(views, url_prefix = "/")

    return app
