#!/usr/bin/python3
"""This module creates a function that works on files"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file

    Args:
        filename of type file
        my_obj of type python object

    Return:
        A pointer to a json file
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f, sort_keys=True)
