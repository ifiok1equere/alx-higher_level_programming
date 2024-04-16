#!/usr/bin/python3
"""This module creates a function that serializes a python object"""
import json


def from_json_string(my_str):
    """
    This function creates an object from a JSON object

    Decoding: JSON to Python Object

    Args:
        my_str of type JSON

    Return:
        A python object
    """

    my_obj = json.loads(my_str)
    return my_obj
