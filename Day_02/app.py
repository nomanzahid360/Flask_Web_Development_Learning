from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html") 

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    users = {
        'Noman':'123',
        'Rizvi':'295'
    }
    
    if username in users and password == users[username]:
        return render_template("welcome.html", name=username)
    else:
        return "Invalid Input"