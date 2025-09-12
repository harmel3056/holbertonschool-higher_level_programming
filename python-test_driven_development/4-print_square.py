#!/usr/bin/python3

"""
This module provides a function that will print
a square of hashes

print_square validates the input and then
prints out the same number of hashes in rows and columns
"""


def print_square(size):
    """
    Prints a square of hashes

    Args:
        size: number of columns and rows of hashes to print
    Returns:
        a printed square of hashes
    Raises:
        TypeError for incorrect entries
        ValueError for numbers entered below 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    column = []
    for qty in range(size):
        print("#" * size)
    return
