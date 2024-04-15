#!/usr/bin/python3

""" This function checks if an object
is an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    This function tests for same instance.

    Args:
        obj: type(any object instance)
        a_class: object class tested against

    Return:
        True or False
    """

    if obj.__class__ == a_class:
        return True
    else:
        return False
