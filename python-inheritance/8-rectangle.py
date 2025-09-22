#!/usr/bin/python3
"""
New class Rectangle which inherits from BaseGeometry and uses its
function integer_validator to validate its input
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        """
        Specifically validates the input and stores it

        Args:
        width - width of the rectangle
        height - height of the rectangle

        Return:
        None, but validated items are stored
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
