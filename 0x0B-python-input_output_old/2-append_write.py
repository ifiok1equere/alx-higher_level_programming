#!/usr/bin/python3
"""This module creates a function that handles files"""


def append_write(filename="", text=""):
    """
    This function appends to a text file

    Endcoding: "UTF-8"

    Args:
        filename of type file
        text of type str

    Return:
        A pointer to the read file
    """

    with open(filename, 'a') as f:
        return f.write(text)
