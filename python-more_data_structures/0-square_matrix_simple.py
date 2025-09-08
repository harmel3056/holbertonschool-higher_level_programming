#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
     result = []
     for row in matrix:
        row_dupe = list(row)
        for element in row_dupe:
            multiple = (element ** 2)
            result += [multiple]
        return result
