#!/usr/bin/python3
"""
Illustrates Duck Typing method with its focus on semantics over
hierarchy. Here we establish an abstract Shape class and use
a basic function to return shape area and perimiter without concern for type
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Defines an abstract class Shape that requires area and perimiter
    methods from its subclasses
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Initialises the Circle class by storing the radius value and then
    running the required methods inherited from Shape parent class

    Args:
    Shape - parent class
    radius - required input for shape outcomes

    Return:
    Area of a Circle
    Perimeter of a Circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi * abs(self.radius) ** 2)

    def perimeter(self):
        return (2 * math.pi * abs(self.radius))


class Rectangle(Shape):
    """
    Initialises the Rectangle class by storing the width and height values
    and then running the required methods inherited from Shape parent class

    Args:
    Shape - parent class
    width - width of the rectangle
    height - height of the rectangle

    Return:
    Area of a Rectangle
    Perimeter of a Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (2 * (self.width + self.height))


def shape_info(argument):
    print("Area: {}".format(argument.area()))
    print("Perimeter: {}".format(argument.perimeter()))


if __name__ == "__main__":
    circle = Circle(radius=-15)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
# Note for this function, the way duck typing operates is to essentially
# see where input types match method intake and then just run it. It's a
# flexible approach to hierarchy/inheritance because it means you don't
# have to define a class for every type of shape - if it looks similar
# it will run.
