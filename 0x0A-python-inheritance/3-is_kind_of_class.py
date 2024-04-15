#!/usr/bin/python3
""" This function checks if an object
is an instance or sub-instance of a specified class"""


def is_kind_of_class(obj, a_class):
    """
    This function tests for same instance/sub-instance.

    Args:
        obj: type(any object instance)
        a_class: object class tested against

    Return:
        True or False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
