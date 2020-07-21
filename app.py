# first we need to import flask
# import render template for rendering
from flask import Flask, render_template, url_for, request

# in order for us to use flask we need to create an instance of our app
# creating a flask instance
app = Flask(__name__)


# syntax for decorators to create a web route
# block of code for default page
@app.route("/")
# create a welcome method to display on homepage
# def index():
    # return "<h1>Welcome to MVC with flask project</h1>"
def welcome_user():
    return render_template("base.html")

@app.route("/login/")
def login_user():
    return render_template("index.html")


# login functionality with GET, POST methods of HTTP
# import requests to use the methods check status code
# add control flow to redirect the user according to their status code received



# index method will be called at the endpoint
# index method will display on our homepage

# syntax to run our app
# if we add debug=True it ensures changes are updated without re-running the app

if __name__ == "__main__":
    app.run(debug=True)


# exercise:- create a function called welcome_user
# create a decorator to link the page /user
# return "welcome to Python flask app dear {user}
# in the browser when we load the page from home page to user name i.e your name
# it should display your name in the browser with message from your methods

# @app.route("/<username>")
# def welcome_user(username):
#     # return f"<h1>Welcome to Python flask app dear {username}</h1>"
#     return render_template("index.html")

# when a error/exception appears - inspect line number at end of error & review your code
# when a error/exception appears - inspect line number at end of error in the browser & review your code
