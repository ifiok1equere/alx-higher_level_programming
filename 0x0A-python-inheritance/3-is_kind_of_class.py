#!/usr/bin/python3
"""This module defines a function that operates on an object"""


def is_kind_of_class(obj, a_class):
    """
    This function checks the instance of an object.

    Args:
        obj: type(obj)
        a_class: class

    Return:
        True if it is an instance
    """

    if isinstance(obj, a_class):
        return True
