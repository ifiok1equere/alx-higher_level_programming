#!/usr/bin/python3
"""This module creates a function that works on files"""
import json


def load_from_json_file(filename):
    """
    This function writes an object from a text file

    Args:
        filename of type file

    Return:
        A pointer to a json file
    """

    with open(filename, 'r') as f:
        return json.load(f)
