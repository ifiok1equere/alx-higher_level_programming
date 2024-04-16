#!/usr/bin/python3
"""This module creates a function that handles files"""


def read_file(filename=""):
    """
    This function reads a text file

    Endcoding: "UTF-8"

    Args:
        filename of type file

    Return:
        A pointer to the read file
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
