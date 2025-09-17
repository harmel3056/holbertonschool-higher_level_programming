#!/usr/bin/python3

"""
Square class which prints a square of the size entered
"""


class Square:
    """
    Square class which prints a square of the size entered

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

    def my_print(self):
        for qty in range(self.size):
            print("#" * self.size)
