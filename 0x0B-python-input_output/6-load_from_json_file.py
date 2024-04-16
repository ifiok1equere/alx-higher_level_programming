#!/usr/bin/python3
"""This module de-serializes"""
import json


def load_from_json_file(filename):
    """Function de-serializes a python object from a file.

    Args:
        filename: file in which object is to be de-serialized from

    Return:
        obj: python data structure after de-serialization
    """

    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.load(f)
    return obj
