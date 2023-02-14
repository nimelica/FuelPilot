from flask import Blueprint ,render_template,request,flash

auth = Blueprint("auth",__name__)

@auth.route("/login",methods=["GET","POST"])
def login():
   return "<p>login</p>"

@auth.route("/logout")
def logout():
    return "<p>logout</p>"

@auth.route("/sign-up",methods=["GET","POST"])
def sign_up():
    return "<p>signup</p>"

