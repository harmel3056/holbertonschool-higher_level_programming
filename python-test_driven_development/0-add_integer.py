#!/usr/bin/python3
"""
This module provides a function that adds two integers.

add_integer validates input types using isinstance and returns
the sum as an integer, even if floats are provided.
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int or float): first number
        b (int or float): second number
    Returns:
        sum of a and b, cast to integer
    Raises:
        TypeError if either argument is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
