#!/usr/bin/python3

""" This function checks if an object
is an instance of a specified class"""


def is_same_class(obj, a_class):
    """

    """
    
    if obj.__class__ == a_class:
        return True
    else:
        return False
