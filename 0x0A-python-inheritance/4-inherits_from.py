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

    if issubclass(obj.__class__, a_class) and (type(obj) != a_class):
        return True
    else:
        return False

    obj_classes = type(obj).__mro__

    return any(cls is not a_class and issubclass(cls, a_class) for cls in obj_classes)
