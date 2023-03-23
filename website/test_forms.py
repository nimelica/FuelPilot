import unittest
from flask import Flask
from .forms import *

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.app_context().push()

# To run the test cases, run this in the terminal:
# python -m unittest website/test_forms.py

class TestInfoForm(unittest.TestCase):
    def test_all_valid(self):
        create_app()
        form = InfoForm(full_name='John Doe',
                        address_1='Center Street',
                        city='Houston',
                        state='TX',
                        zipcode='77777')
        print('\nTesting InfoForm for All Valid')
        self.assertTrue(form.validate())

    def test_some_valid(self):
        create_app()
        form = InfoForm(full_name='This is a very long name that exceeds the maximum length allowed by the validator',
                        address_1='Center Street',
                        city='Houston',
                        state='TX',
                        zipcode='7777777777777')
        print('\nTesting InfoForm for Some Valid')
        self.assertFalse(form.validate())

    def test_none_valid(self):
        create_app()
        form = InfoForm(full_name='This is a very long name that exceeds the maximum length allowed by the validator',
                        address_1='This is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validator',
                        city='This is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validator',
                        state='This is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validatorThis is a very long name that exceeds the maximum length allowed by the validator',
                        zipcode='7777777777777')
        print('\nTesting InfoForm for None Valid')
        self.assertFalse(form.validate())


class TestQuoteFuelForm(unittest.TestCase):    
    def test_all_valid(self):
        create_app()
        form = QuoteFuelForm()
        self.assertTrue(form.validate())

    def test_some_valid(self):
        create_app()
        form = QuoteFuelForm()
        self.assertFalse(form.validate())

    def test_none_valid(self):
        create_app()
        form = QuoteFuelForm()
        self.assertFalse(form.validate())