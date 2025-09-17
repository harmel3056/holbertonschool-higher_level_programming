#!/usr/bin/python3
"""
Square class which returns the current square of the size
"""


class Square:
    """
    Square class which returns the current square of the size

    Args:
    size=0

    Return:
    Square of the size entered
    TypeError or ValueError for incorrect entries
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
