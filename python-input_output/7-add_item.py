#!/usr/bin/python3
"""
Adds python arguments to an existing list,
or creates a new list, and then returns that list
as a JSON file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    data = load_from_json_file(filename)
    if not isinstance(data, list):
        data = []
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
