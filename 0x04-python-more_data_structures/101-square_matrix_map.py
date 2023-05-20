#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda y: [x ** 2 for x in y], matrix))
