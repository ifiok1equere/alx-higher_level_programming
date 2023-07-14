#!/usr/bin/python3
"""
This module defines a division function for a matrix.
All elements of the matrix are divided by an integer
and the result is the resulting matrix after division.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies a matrix by another matrix.

    Args:
        m_a: 1st Matrix argument.
        m_b: 2nd Matrix argument.

    Return:
        A matrix
    """

    if not isinstance(m_a, list):
        raise TypeError(
                "m_a must be a list"
                )

    if not isinstance(m_b, list):
        raise TypeError(
                "m_b must be a list"
                )

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError(
                "m_a must be a list of lists"
                )

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError(
                "m_b must be a list of lists"
                )

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(item, (int, float)) for
               row in m_a for item in row):
        raise TypeError(
                "m_a should contain only integers or floats"
                )

    if not all(isinstance(item, (int, float)) for
               row in m_b for item in row):
        raise TypeError(
                "m_b should contain only integers or floats"
                )

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_a_row = len(m_a)
    m_a_column = len(m_a[0])
    m_b_row = len(m_b)
    m_b_column = len(m_b[0])
    new_matrix = []

    """ Create an empty result array """
    for _ in range(m_a_row):
        new_matrix.append([0] * m_b_column)

    """ Perform matrix multiplication """
    for i in range(m_a_row):
        for j in range(m_b_column):
            for k in range(m_a_column):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
