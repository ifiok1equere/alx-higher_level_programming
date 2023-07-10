#!/usr/bin/python3
"""This module defines a function that operates on an object"""


def inherits_from(obj, a_class):
    """
    This function checks the instance of an object.

    Args:
        obj: type(obj)
        a_class: class

    Return:
        True if it is an instance
    """

    if issubclass(obj.__class__, a_class) and (type(obj) is a_class):
        return False
    else:
        return True
