#!/usr/bin/python3
"""
Returns the object that was represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Converts JSON string to Python object

    Args:
    my_str - JSON string to convert

    Return:
    Python object converted from JSON string
    """
    data = json.loads(my_str)
    return data
