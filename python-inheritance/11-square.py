#!/usr/bin/python3
"""
Uses inheritance to produce a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Uses inheritance to produce a square

    Args:
    Takes Rectangle class as parent class

    Return:
    Formatted string and the area
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__size, self.__size)
