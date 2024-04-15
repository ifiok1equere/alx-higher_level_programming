#!/usr/bin/python3
"""This function returns the list of object attr's and meth's"""


def lookup(obj):
    """
    This function defines an object obj.

    Args:
        obj: type(obj)

    Return:
        Attribute and methods of the object
        instance
    """

    return(dir(obj))
