from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def std_profile():
    return render_template(
        "std_profile.html",
        name = "Noman",
        is_topper = True,
        subjects = ["Math", "CS", "SE"]
    )