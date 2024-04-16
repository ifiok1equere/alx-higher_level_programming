#!/usr/bin/python3
"""This module de-serializes"""
import json


def from_json_string(my_obj):
    """Function de-serializes a python object.

    Args:
        my_obj: python object to be de-serialized

    Return:
        Python data structure
    """

    return json.loads(my_obj)
