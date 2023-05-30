#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    fro i in range(1, 4):
        result += b ** 1
    if result > a:
        raise Exception("Too far")
    return result / a
