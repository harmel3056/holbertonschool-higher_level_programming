#!/usr/bin/python3
"""
Returns a dictionary from a class,
ready for JSON serialization
"""


def class_to_json(obj):
    """
    Returns a dictionary from a class,
    ready for JSON serialization

    Args:
    obj - object from a class to serialize

    Return:
    dictionary of the objects contents
    """
    return obj.__dict__
