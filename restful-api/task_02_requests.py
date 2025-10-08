#!/usr/bin/python3
"""
"""
import requests

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    data = response.json()
    print(data)

    # api_url = "https://jsonplaceholder.typicode.com/posts/1"
    # response = requests.get(api_url)

    # # Check if the request was successful
    # if response.status_code == 200:
    #     # Print the JSON content of the response
    #     data = response.json()
    #     print("Successfully retrieved data:")
    #     print(data)
    # else:
    #     print(f"Failed to retrieve data. Status code: {response.status_code}")

fetch_and_print_posts()