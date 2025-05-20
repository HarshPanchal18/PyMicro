from flask import Flask, request, jsonify, render_template, session, redirect
from pymongo import MongoClient


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

# MongoDB setup
client = MongoClient(f"{MONGO_CONN_STR}")
db = client["user_db"]
users_collection = db["users"]

# (Optional) Pre-insert a test user
if not users_collection.find_one({"username": "admin"}):
    users_collection.insert_one({"username": "admin", "password": "admin"})


@app.route("/users", methods=["GET"])
def get_users():
    username = request.args.get("username")
    password = request.args.get("password")
    user = users_collection.find_one({"username": username, "password": password})
    return jsonify({"exists": bool(user)})


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    return redirect(f"http://{LOGIN_IP}:{LOGIN_PORT}/")  # Redirect to login service

if __name__ == "__main__":
    app.run(port=DASHBOARD_PORT, host="0.0.0.0")
