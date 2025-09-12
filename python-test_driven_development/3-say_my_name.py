#!/usr/bin/python3

"""
This module provides a function that prints first and last names
entered

say_my_name validates the input and then
inserts each element accordingly
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name

    Args:
        first_name: first name entered
        last_name: last name entered
    Returns:
        a string with the names inserted within
    Raises:
        TypeError for incorrect entries
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
