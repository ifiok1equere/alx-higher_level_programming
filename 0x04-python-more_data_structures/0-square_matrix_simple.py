#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix == None:
        return
    new_matrix = []
    #new_matrix = [row[:] for row in matrix]
    for row in matrix:
        new_matrix.append(row[:])
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix)):
                new_matrix[i][j] *= new_matrix[i][j]
    return (new_matrix)
