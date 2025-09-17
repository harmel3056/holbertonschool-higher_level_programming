#!/usr/bin/python3
"""
Rectangle class that gives perimiter and area, and returns
sick-as hash rectangle. Accommodates eval() with __repr__ too.
This version introduces a counter to keep track of the
instances of rectangle
"""


class Rectangle:
    """
    A class definition of the rectangle including input values
    and entry limitations. Returns perimeter and area, and
    prints # grids with those args.

    Args:
    width - defines the width of the rectangle as an int
    height - defines the height of the rectangle as an int

    Return:
    Area and Perimeter, and __str__ grid to print visual representation
    """
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rows = []
        for qty in range(self.height):
            rows.append("#" * self.width)
        return "\n".join(rows)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
