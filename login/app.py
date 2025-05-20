from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
import requests

app = Flask(__name__)
app.secret_key = 'login_secret'
Session(app)

USERS_API = "http://localhost:5001/users"  # dashboard_service hosts the user API

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Call the user API from dashboard service
        response = requests.get(USERS_API, params={"username": username, "password": password})
        if response.json().get("exists"):
            session["username"] = username
            return redirect("http://localhost:5001/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
