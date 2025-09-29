#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
    my_obj - data to write in JSON format
    filename - file to write data to

    Return:
    Nothing on its own, will facilitate writing
    """
    with open(filename, "w", encoding="UTF-8") as f:
        data = f.write(json.dumps(my_obj))
    return data
