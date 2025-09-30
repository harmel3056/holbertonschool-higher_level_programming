#!/usr/bin/python3
"""
Builds a Pascal Triangle of size n
"""


def pascal_triangle(n):
    """
    Builds a Pascal Triangle of size n

    Args:
    n - number of rows and ultimate columns
    """

    triangle = []

    for currt_row in range(n):
        row = []
        for element in range(currt_row + 1):
            if element == 0 or element == currt_row:
                row.append(1)
            else:
                value = triangle[currt_row-1][element-1] + \
                    triangle[currt_row-1][element]
                row.append(value)
        triangle.append(row)
    return triangle
