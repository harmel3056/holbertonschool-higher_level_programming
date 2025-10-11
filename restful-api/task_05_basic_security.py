#!/usr/bin/python3
"""
Basic API with a focus on Security and Authentication tecniques
"""
from flask import Flask
from flask import request, jsonify

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "dev-secret-1234-xyz"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },

    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username

@app.route('/basic-protected', methods = ['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods = ['POST'])
def login():
    #takes input from POST
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)

    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 401

    if not user:
        return jsonify({"msg": "Username or password not identified"}), 401
    
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]}
            )
        return jsonify(access_token=access_token)

    else:
        return jsonify({"msg": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods = ['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"msg": "JWT Auth: Access Granted"})

@app.route("/admin-only", methods = ['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt()
    if current_user.get("role") == "admin":
        return jsonify({"msg": "Admin Access: Granted"})
    else:
        return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run()
