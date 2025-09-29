#!/usr/bin/python3
"""
Returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Converts an object to its JSON representation

    Args:
    object to be converted to JSON format

    Return:
    JSON version of that object
    """
    data = json.dumps(my_obj)
    return data
