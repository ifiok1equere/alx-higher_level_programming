#!/usr/bin/python3
"""This module serializes"""
import json


def save_to_json_file(my_obj, filename):
    """Function serializes a python object and writes into a file.

    Args:
        my_obj: python object to be serialized
        filename: file in which object is to be saved into

    Return:
        None
    """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
