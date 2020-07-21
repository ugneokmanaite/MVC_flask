from flask import Flask

# in order for us to use flask we need to create an instance of our app

# creating a flask instance
app = Flask(__name__)


# syntax for decorators to create a web route
# block of code for default page
@app.route("/")
# create a welcome method to display on homepage
def index():
    return "<h1>Welcome to MVC with flask project</h1>"


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

@app.route("/<name>")
def welcome_user(name):
    return f"<h1>Welcome to Python flask app dear {name}</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)
