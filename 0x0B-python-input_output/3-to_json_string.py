#!/usr/bin/python3
"""This module serializes"""
import json


def to_json_string(my_obj):
    """Function appends to a text file (UTF8)

    Args:
        my_obj: python object to be serialized

    Return:
        JSON representation of an object (string)
    """

    return json.dumps(my_obj)
