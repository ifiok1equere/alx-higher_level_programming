#!/usr/bin/python3
"""
This module defines an addition functions for integers.
No other basic mathematical operations are covered therein
except the addition operation and some checks with it.
"""


def add_integer(a, b=98):
    """ Adds two numbers together.
    Args:   a (int): The first number.
            b (int): The second number. """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
