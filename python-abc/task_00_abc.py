#!/usr/bin/python3
"""
This module defines a class hierarchy using inheritance.
It specifically focuses on abstract method and how that is
used in concrete classes
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Defines a class called Animal and sets an abstract method
    for subclasses to all include the sound function
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Concrete subclass of Animal that represents a dog

    Return:
    Returns the sound "Bark"
    """
    def sound(self):
        return ("Bark")

class Cat(Animal):
    """
    Concrete subclass of Animal that represents a cat

    Return:
    Returns the sound "Meow"
    """
    def sound(self):
        return ("Meow")
