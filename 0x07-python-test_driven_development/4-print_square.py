#!/usr/bin/python3
"""
This module defines a function detailing a square.
This function defines a sqaure of n number of sides
which is used to print the square.
"""


def print_square(size):
    """ Function that prints a square with the character #.
    Args:   Matrix: The first argument.
            div (int): The divisor. """

    if not isinstance(size, int):
        raise TypeError(
                "size must be an integer"
                )
    if size < 0:
        raise ValueError(
                "size must be >= 0"
                )

    if isinstance(size, float) and size < 0:
        raise TypeError(
                "size must be an integer"
                )
    i = 0
    while i < size:
        print('#' * size)
        i += 1
