import unittest
from flask import Flask
from .forms import InfoForm

class TestInfoForm(unittest.TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_InfoForm(self):
        app = self.create_app()
        app.app_context().push()
        form = InfoForm(full_name='John Doe',
                        address_1='Center Street',
                        city='Houston',
                        state='TX',
                        zipcode='77777')
        self.assertTrue(form.validate())




