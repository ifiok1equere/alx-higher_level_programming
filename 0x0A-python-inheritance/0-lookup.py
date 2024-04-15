#!/usr/bin/python3

'''
This function returns the list of available
attributes and methods of an object.
'''


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
