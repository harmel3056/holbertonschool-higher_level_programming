#!/usr/bin/python3
"""
Square class that handles size as int >= 0 only
"""


class Square:
    """
    Square class that handles size as int >= 0 only

    Args:
    size=0

    Return:
    TypeError or ValueError for incorrect entries
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
