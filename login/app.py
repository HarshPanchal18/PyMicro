from flask import Flask, request, render_template, redirect, session
import requests
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

load_dotenv()
MONGO_CONN_STR = os.environ.get("MONGO_CONN_STR")
LOGIN_PORT = os.environ.get("LOGIN_PORT")
LOGIN_IP = os.environ.get("LOGIN_IP")
DASHBOARD_PORT = os.environ.get("DASHBOARD_PORT")
DASHBOARD_IP = os.environ.get("DASHBOARD_IP")
SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)
app.secret_key = SECRET_KEY

USERS_API = f"http://{DASHBOARD_IP}:{DASHBOARD_PORT}/users"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        logging.info(f"Login attempt for user: {username}")
        try:
            response = requests.get(USERS_API, params={"username": username, "password": password})
            logging.info(f"Requested {USERS_API} with params: username={username}")
            response.raise_for_status()
            exists = response.json().get("exists")
            logging.info(f"User exists: {exists}")
        except Exception as e:
            logging.error(f"Error during user API request: {e}")
            return render_template("login.html", error="Service unavailable")

        if exists:
            session["username"] = username
            logging.info(f"User {username} logged in successfully.")
            return redirect(f"http://{DASHBOARD_IP}:{DASHBOARD_PORT}/dashboard")
        else:
            logging.warning(f"Invalid credentials for user: {username}")
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

if __name__ == "__main__":
    logging.info(f"Starting app on {LOGIN_IP}:{LOGIN_PORT}")
    app.run(host="0.0.0.0", port=int(LOGIN_PORT))
