#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a += 0, 0
    if len(tuple_b) == 0:
        tuple_b += 0, 0
    if len(tuple_a) < 2:
        tuple_a += 0,
    if len(tuple_b) < 2:
        tuple_b += 0,
    a, b = tuple_a[0], tuple_a[1]
    c, d = tuple_b[0], tuple_b[1]
    new_tuple = a + c, b + d
    return (new_tuple)
