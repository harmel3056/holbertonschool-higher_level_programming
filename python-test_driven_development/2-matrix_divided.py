#!/usr/bin/python3

"""
This module provides a function that divides elements of a matrix
using the provided divisor

matrix_divided validates the input first, and then methodically
divides each element one by one.
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix

    Args:
        matrix: the entire matrix to be divided
        div: the divisor to use against the matrix
    Returns:
        a new matrix with the same format but divided content
    Raises:
        TypeError for incorrect entries
        ZeroDivisionError for div=0
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row = 0
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
