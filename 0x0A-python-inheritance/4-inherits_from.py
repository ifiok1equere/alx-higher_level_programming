#!/usr/bin/python3
"""This function checks if an object is a sub-instance"""


def inherits_from(obj, a_class):
    """
    This function tests for sub-class.

    Args:
        obj: type(any class)
        a_class: object class tested against

    Return:
        True or False
    """

    if isinstance(obj, a_class) and (type(obj) != a_class):
        return True
    else:
        return False
