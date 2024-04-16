#!/usr/bin/python3
"""This module defines a function"""


def class_to_json(obj):
    """This function serializes an object

    Args:
        obj: Python object to be serialized

    Return:
        dictionary description with simple data structure
    """

    return obj.__dict__
