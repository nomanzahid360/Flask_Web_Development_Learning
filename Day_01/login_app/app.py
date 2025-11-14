from flask import Flask, request, redirect, Response, url_for, session

app = Flask(__name__)
app.secret_key = "superkey"

# Login Page
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "noman" and password == "123":
            session["user"] = username # Store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Input", mimetype="text/plain")
    
    return '''
        <h2>Login Page </h2>
        <form method = "POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>
        '''

# Welcome Page (After Login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2> Welcome {session["user"]}!</h2>
            <a href={url_for('logout')}> Logout </a>
        '''
    return redirect(url_for("login"))

# Logout Page
@app.route("/logout")
def logout():
    session.pop("user", None)

    return redirect(url_for("login"))