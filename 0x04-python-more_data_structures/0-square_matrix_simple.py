#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix == []:
        return
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[:])
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix)):
            new_matrix[i][j] = matrix[i][j] ** 2
    return (new_matrix)
