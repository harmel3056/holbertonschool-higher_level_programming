#!/usr/bin/python3
"""
Defines the Rectangle class in greater detail
"""


class Rectangle:
    """
    A definition of the rectangle including input values
    and entry limitations

    Args:
    width - defines the width of the rectangle as an int
    height - defines the height of the rectangle as an int

    Return:
    None
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
