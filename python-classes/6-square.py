#!/usr/bin/python3

"""
Square class which prints a square of the size entered
"""


class Square:
    """
    Square class which prints a square of the size entered
    Also takes position to determine placement

    Args:
    size - size of the square in height and width
    position - [0] denotes spaces before the #
    [1] denotes empty lines before entries begin

    Return:
    Square of the size and placement entered
    TypeError or ValueError for incorrect entries
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(v, int) and v >= 0 for v in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for qty in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
