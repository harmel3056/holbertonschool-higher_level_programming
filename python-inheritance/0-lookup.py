#!/usr/bin/python3
"""
lookup returns a list of attributes and methods of an object
"""


def lookup(obj):
    """
    returns a list of attributes and methods of an object

    Args:
    object - object whose attributes will be returned

    Return:
    list of attributes and methods of an object
    """
    return dir(obj)
