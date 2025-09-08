#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        row_dupe = list(row)
        squared_row = []
        for element in row_dupe:
            squared_row.append(element ** 2)
        result.append(squared_row)
    return result
