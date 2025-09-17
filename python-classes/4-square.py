#!/usr/bin/python3

"""
Square class which returns the current square of the size
"""


class Square:
    """
    Square class which returns the current square of the size
    with emphasis on getter and setter method

    Args:
    size=0

    Return:
    Square of the size entered
    TypeError or ValueError for incorrect entries
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
