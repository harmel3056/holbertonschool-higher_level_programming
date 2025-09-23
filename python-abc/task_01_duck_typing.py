#!/usr/bin/python3
"""
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        area = math.pi * radius ** 2
        perimeter =  2 * math.pi * radius

class Rectangle(Shape):
    def __init__(self, width, height):
        area = width * height
        perimeter = 2 * (width + height)

def shape_info(argument):
    print(argument.area())
    print(argument.perimeter)
    # print("Area: {}".format(area))
    # print("Perimeter: {}".format(perimeter))