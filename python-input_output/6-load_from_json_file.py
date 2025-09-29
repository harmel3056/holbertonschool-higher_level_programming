#!/usr/bin/python3
"""
creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
    filename - name of the file to convert to object

    Return:
    object version of the file's contents
    """
    with open(filename, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data
