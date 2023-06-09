#!/usr/bin/python3
"""This module defines a function that operates on an object"""


def is_same_class(obj, a_class):
    """
    This function checks for exactness of an instance.

    Args:
        obj: type(obj)
        a_class: class

    Return:
        True if exact
    """

    return type(obj) is a_class
