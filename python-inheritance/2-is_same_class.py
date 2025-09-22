#!/usr/bin/python3
"""
Specifically identifies if an object is of the same type
as that specified. Inheritance is disregarded.
"""


def is_same_class(obj, a_class):
    """
    Returns whether an object is the same type specified

    Input:
    obj - object to check type of
    a_class - type to match

    Return:
    True for an exact match
    False where exact match not found
    """
    if type(obj) is a_class:
        return True
    else:
        return False
