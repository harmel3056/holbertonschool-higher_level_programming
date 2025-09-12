#!/usr/bin/python3
"""
This module provides a function that prints a reformatted
version of the string that is entered
"""


def text_indentation(text):
    """
    Reformats a string using the ?.: denominators

    Args:
        text: a string
    Returns:
        string printed with newlines whereever ?.: occur
    Raises:
        TypeError for incorrect entries
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    skip_space = False

    for char in text:
        if skip_space and char == " ":
            continue

        skip_space = False

        new_text += char
        if char in ".?:":
            new_text += "\n\n"
            skip_space = True

    print(new_text.strip(), end="")
