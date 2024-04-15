#!/usr/bin/python3
""" This function checks if an object
is an instance or sub-instance of a specified class"""


def inherits_from(obj, a_class):
    """
    This function tests for sub-class.

    Args:
        obj: type(any class)
        a_class: object class tested against

    Return:
        True or False
    """

    if type(obj) != a_class:
        return True
    else:
        return False
