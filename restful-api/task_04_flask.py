#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users_data = {}

@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"

@app.route("/data")
def data():
    print("serving/data", users_data)
    return jsonify(users_data)

@app.route("/status")
def status():
    return "<p>OK</p>"

@app.route("/users/<username>")
def users(username):
    return f"{username}"

@app.route("/add_user", methods=["POST"])
def add_user():
    parsed = request.get_json()
    users_data[parsed["username"]] = {
        "name": parsed["name"],
        "age": parsed["age"],
        "city": parsed["city"]
    }
    print("add_user complete")
    return jsonify(users_data)



if __name__ == "__main__": 
    app.run()
