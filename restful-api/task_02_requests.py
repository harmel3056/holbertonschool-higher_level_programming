#!/usr/bin/python3
"""
Exploring post retrieval methods using requests
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Retrieves posts and prints the status code followed
    by a list of titles
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for title in [post['title'] for post in data]:
            print(title)
# fetch_and_print_posts():


def fetch_and_save_posts():
    """
    Retrieves posts and converts them to CSV format
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        rows = [
            {'id': post['id'], 'title': post['title'],
             'body': post['userId']}
            for post in data
        ]

        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
fetch_and_save_posts()
