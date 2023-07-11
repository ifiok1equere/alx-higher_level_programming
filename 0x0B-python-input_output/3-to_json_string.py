#!/usr/bin/python3
"""This module creates a function that serializes a python object"""
import json


def to_json_string(my_obj):
    """
    This function creates a JSON rep of a python object

    Endcoding: JSON

    Args:
        filename of type file
        text of type str

    Return:
        A pointer to the read file
    """

    my_obj_json = json.dumps(my_obj, sort_keys=True)
    return my_obj_json
