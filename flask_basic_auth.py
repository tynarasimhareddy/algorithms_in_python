from flask import Flask
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)



#Order of below decorator is important
@app.route('/', methods = ['GET'])
@auth.login_required
def hello():
    return "Hello Narasimha Reddy"

#Below is the call_back method invoked with passed user, pswd
@auth.verify_password
def verify_password(user, pswd):
    # define your own authentication logic
    if user == 'admin' and pswd == 'admin':
        return True
    return False

app.run(host='localhost', port=8080, debug=True)
