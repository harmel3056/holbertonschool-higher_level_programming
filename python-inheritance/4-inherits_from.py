#!/usr/bin/python3
"""
Identifies when an object is a subject of inheritance from
the specified class
"""


def inherits_from(obj, a_class):
    """
    Identifies when object is an instance of inheritance
    from the class entered

    Args:
    obj - object to analyse
    a_class - class to check for inheritance

    Return:
    True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified
    class, otherwise False.
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
