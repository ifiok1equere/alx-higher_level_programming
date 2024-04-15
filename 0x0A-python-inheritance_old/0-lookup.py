#!/usr/bin/python3
"""This module defines a function that operates on an object"""


def lookup(obj):
    """
    This function defines an object obj.

    Args:
        obj: type(obj)

    Return:
        Attribute and methods of the object
        instance
    """

    return (dir(obj))
