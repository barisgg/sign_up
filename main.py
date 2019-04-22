from flask import Flask, request
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True    

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


welcomeMessage = """
<h1>Welcome to my super cool page!</h1>
<a href="/register">Register</a> """

@app.route("/register", methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    usernameError = ""
    passwordError = ""
    password2Error = ""
    emailError = ""

    if not username:
        usernameError = "Username is required"
    if len(username) < 3 or len(username) > 20:
        usernameError = "Username must be 3 to 20 characters long"
    for char in username:
        if char.isalpha() is False:
            usernameError = "Username can't contain a space"
    
    if not password:
        passwordError = "Password is required"
    elif len(password) < 3 or len(username) > 20:
        passwordError = "Password must be 3 to 20 characters long"
    else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError = "Password must contain a number"
    for char in password:
        if char == " ":
            passwordError = "Password can't contain a space"
    if password  != password2:
        password2Error = "Passwords do not match" 

    period = 0
    for char in email:
        if char == "." or char == "@":
            period += 1
    if period > 2:
        emailError = "Email must contain one period and one @"
    elif period < 2:
        emailError = "Email must contain one period and one @"
    else: 
        email = request.form['email']
        emailError == ""
        if char == " ":
            emailError = "Email can't contain a space"
    if len(email) < 3 or len(email) >20:
        emailError = "Email must be between 3 to 20 characters long"
    

    
    if usernameError or passwordError or password2Error:
        print("there was an error!")
        content = jinja_env.get_template('form.html')
        return content.render(email=email,emailError=emailError, username=username,one=usernameError,three=passwordError,five=password2Error)

    validated = jinja_env.get_template('thanks.html')
    return validated.render(name=username)


@app.route("/")
def index():
    # build the response string
    
    body = jinja_env.get_template('form.html')
    return body.render(body=body)

@app.route("/register", methods=['GET'])
def register_page():
    # build the response string
    body = jinja_env.get_template('form.html')
    return body.render(body=body)

app.run()

## Cross Site scripting
# <script>alert("HEHEHEHE")</script>