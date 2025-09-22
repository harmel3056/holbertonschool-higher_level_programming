#!/usr/bin/python3
"""
Class that validates entries based on type
"""


class BaseGeometry:
    """
    Class that validates entries based on type

    Args:
    None

    Return:
    Exceptions, TypeErrors, ValueErrors based on your entries
    """
    def area(self):
        """
        Raises an exception indicating area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer

        Args:
        name (str): name of the value (used in error messages)
        value (int): the value to validate

        Raises:
        TypeError if 'value' is not an integer
        ValueError if 'value' is not a positive number
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
