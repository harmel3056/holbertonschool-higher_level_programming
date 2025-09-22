#!/bin/usr/python3
"""
Class that raises an exception
"""


class BaseGeometry:
    """
    Class that raises an exception

    Args:
    None

    Return:
    raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")
