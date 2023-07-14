#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2, 6]], [[3, 4], [5, 6], [9, 0]]))
print(matrix_mul([[1, 2], [5, 7.3]], [[3, 4, 1.8], [5, 0, 6]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 5, 9], [4, 5.5, 7.3]], [[3, 4], [5, 6]]))
