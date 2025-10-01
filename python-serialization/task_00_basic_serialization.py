#!/usr/bin/python3
"""
Basic serialization module that adds the functionality to
serialize a Python dictionary to a JSON file and deserialize
the JSON file to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes and saves data to the specified file

    Args:
    data - data to be serialized and saved
    filename - name of the file to save the data to
    """
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    Opens the file and deserializes the data to Python dict

    Args:
    filename - name of the JSON input file

    Return:
    Python dict deserialized from JSON input file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
