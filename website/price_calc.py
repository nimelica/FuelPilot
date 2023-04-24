from flask import Blueprint ,render_template, session, flash, redirect, url_for, request
from .models import *

def calculatePricing(gallons_requested, state):
    Location_Factor = 0.02 if state == 'TX' else 0.04
    user_id = session.get('user_id')
    fuel_quotes = FuelQuote.query.filter_by(client_id=user_id).all()
    Rate_History_Factor = 0.01 if len(fuel_quotes) != 0 else 0.00
    Gallons_Requested_Factor = 0.03 if gallons_requested < 1000 else 0.02
    Company_Profit_Factor = 0.10
    Current_Price_Per_Gallon = 1.50
    Margin = Current_Price_Per_Gallon * (Location_Factor - Rate_History_Factor + Gallons_Requested_Factor + Company_Profit_Factor)
    Suggested_Price_Per_Gallon = Current_Price_Per_Gallon + Margin
    Total_Amount_Due = gallons_requested * Suggested_Price_Per_Gallon
    return Suggested_Price_Per_Gallon, Total_Amount_Due
