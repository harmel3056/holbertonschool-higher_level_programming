#!/usr/bin/python3

import requests

BASE_URL = "http://localhost:5000"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    print("GET /:", response.text)

def test_data():
    response = requests.get(f"{BASE_URL}/data")
    print("GET /data:", response.json())

def test_status():
    response = requests.get(f"{BASE_URL}/status")
    print("GET /status:", response.text)

def test_dynamic_user():
    response = requests.get(f"{BASE_URL}/users/john")
    print("GET /users/john:", response.text)

def test_add_user():
    new_user = {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=new_user)
    print("POST /add_user:", response.json())

def run_all_tests():
    print("Running tests against task_04_flask.py...\n")
    test_home()
    test_data()
    test_status()
    test_dynamic_user()
    test_add_user()

if __name__ == "__main__":
    run_all_tests()