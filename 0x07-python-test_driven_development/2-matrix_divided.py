#!/usr/bin/python3
"""
This module defines a division function for a matrix.
All elements of the matrix are divided by an integer
and the result is the resulting matrix after division.
"""


def matrix_divided(matrix, div):
    """ Divides a matrix by an integer.
    Args:   Matrix: The first argument.
            div (int): The divisor. """

    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not all(isinstance(item, (int, float)) for
               row in matrix for item in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)
    return new_matrix
