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
        form = QuoteFuelForm(gallons_requested =2,
                             delivery_address='main street',
                             delivery_date= '03/01/2023',
                             suggested_price=5,
                             total_amount_due=10
                            )
        self.assertTrue(form.validate())

    def test_some_valid(self):
        create_app()
        form = QuoteFuelForm(gallons_requested =0,
                             delivery_address='holly hall',
                             delivery_date='04/01/2023',
                             suggested_price=10,
                             total_amount_due=20)
        self.assertFalse(form.validate())

    def test_none_valid(self):
        create_app()
        form = QuoteFuelForm(gallons_requested =0,
                             delivery_address='scott st',
                             delivery_date='05/01/2023',
                             suggested_price=20,
                             total_amount_due=30)
        self.assertFalse(form.validate())
