## MVC

- model view controller
- industry standard framework used across different languages

_What is it?_
<img src="https://www.guru99.com/images/1/122118_0445_MVCTutorial1.png">

# Importing flask
`from flask import Flask`

# In order for us to use flask we need to create an instance of our app
`app = Flask(__name__)`

# Decorators for homepage
`@app.route("/")`

# Create a welcome method to display on homepage
```python
def index():

    return "<h1>Welcome to MVC with flask project</h1>"
```

- index method will be called at the endpoint
- index method will display on our homepage

# Running out app 
```python
if __name__ == "__main__":
    app.run(debug=True)
```
    
# exercise:- create a function called welcome_user
`create a decorator to link the page /user`

`return "welcome to Python flask app dear {user}`

`in the browser when we load the page from home page to user name i.e your name`

`it should display your name in the browser with message from your methods`

```python
@app.route("/<name>")
def welcome_user(name):
    return f"<h1>Welcome to Python flask app dear {name}</h1>"
```
