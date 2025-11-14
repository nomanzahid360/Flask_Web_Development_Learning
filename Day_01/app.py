from flask import Flask, request

app = Flask(__name__) # --> Create an object. Represent Our Website (Main File)

'''
Specifications for Route 
    01- Unique Route Name
    02- Readable Route Name
    03- Always Return Something
'''

@app.route("/") # Route Path
def home():
    return "Hi, My First Flask Project" 

@app.route("/about")
def about():
    return 'This is About Page'

# ---------------------------------

'''
Get Method:
    Get Data
    Give You Something
    Don't Sent Data
    Example: (Visit Webpage Only)
Post Method:
    Send Data --> Server
    It does something
    Example: (Login | Register)
'''

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You send Data"
    else:
        return "You are only viewing the form"