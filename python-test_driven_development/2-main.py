#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)


# Division by positive infinity
print(matrix_divided(matrix, float("inf")))

# Division by negative infinity (should also be 0.0)
print(matrix_divided(matrix, float("-inf")))
