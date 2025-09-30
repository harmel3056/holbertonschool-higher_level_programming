#!/usr/bin/python3
"""
Uses list comprehension to filter input instances
of class attributes that match our established class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instanstiates a library of attributes for the
        Student class
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
        filters input attributes to only return those
        in Student class, then converts the relevant
        fields to a dictionary for output
        """
        if isinstance(attrs, list) and attrs is not None:
            self.__dict__ = {key: self.__dict__[key]
                             for key in attrs if key in self.__dict__}

        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Takes values from json dict and writes them to
        existing Student class
        """
        for key, value in json.items:
            if key in self.__dict__:
                setattr(self, key, value)

        return self.__dict__.copy()
