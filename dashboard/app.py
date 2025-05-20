from flask import Flask, request, jsonify, render_template, session, redirect
from flask_session import Session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'dashboard_secret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
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
    return redirect("http://localhost:5000/")  # Redirect to login service

if __name__ == "__main__":
    app.run(port=5001, debug=True)
