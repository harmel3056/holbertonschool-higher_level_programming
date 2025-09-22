#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
New class Rectangle which inherits from BaseGeometry and uses its
function integer_validator to validate its input
"""


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry to validate width and height, and
    then assigns their values

    Args:
    BaseGeometry - a separate class which aids in validation

    Return:
    None
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
