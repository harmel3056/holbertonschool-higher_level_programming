#!/usr/bin/python3
"""
Develop a simple API using Python with Flask
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

app = Flask(__name__)
users_data = {}


@app.route("/")
def home():
    return Response("Welcome to the Flask API!",
                    status=200, mimetype="text/plain")


@app.route("/data")
def data():
    names_list = [username for username in users_data]
    return jsonify(names_list)


@app.route("/status")
def status():
    return Response("OK", status=200, mimetype="text/plain")


@app.route("/users/<username>")
def get_user(username):
    user = users_data.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    parsed = request.get_json()
    username = parsed.get("username")

    # if "username" not in parsed or not parsed["username"]:
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # users_data[parsed["username"]] = {
    #     "name": parsed["name"],
    #     "age": parsed["age"],
    #     "city": parsed["city"]
    # }

    users_data[username] = parsed

    return jsonify({
        "message": "User added successfully",
        "user": users_data[parsed["username"]]
    }), 201


if __name__ == "__main__":
    app.run()
