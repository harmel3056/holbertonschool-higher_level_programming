#!/usr/bin/python3
"""
"""
import requests
import json

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "dev-secret-1234-xyz"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

User = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@app.route('/private')
@auth.login_required
def private():
    return "Welcome!"

@app.login('/login', methods = ['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/dashboard")
@jwt_required()
def dashboard():
    user = get_jwt_identity()
    return jsonify(message=f"Welcome back, {user}")









@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username