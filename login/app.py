from flask import Flask, request, render_template, redirect, session
import requests


import os
from dotenv import load_dotenv
load_dotenv()
MONGO_CONN_STR=os.environ.get("MONGO_CONN_STR")
LOGIN_PORT=os.environ.get("LOGIN_PORT")
LOGIN_IP=os.environ.get("LOGIN_IP")
DASHBOARD_PORT=os.environ.get("DASHBOARD_PORT")
DASHBOARD_IP=os.environ.get("DASHBOARD_IP")
SECRET_KEY=os.environ.get("SECRET_KEY")

app = Flask(__name__)
app.secret_key = SECRET_KEY
# Session(app)

USERS_API = f"http://{DASHBOARD_IP}:{DASHBOARD_PORT}/users"  # dashboard_service hosts the user API

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Call the user API from dashboard service
        response = requests.get(USERS_API, params={"username": username, "password": password})
        if response.json().get("exists"):
            session["username"] = username
            return redirect(f"http://{DASHBOARD_IP}:{DASHBOARD_PORT}/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LOGIN_PORT)
