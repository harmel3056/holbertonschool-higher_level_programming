#!/usr/bin/python3
"""
Establishes Student class and then converts
it to dictionary for JSON serialization
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instanstiates a library of attributes for the
        Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the Student class to a dictionary
        """
        return self.__dict__
