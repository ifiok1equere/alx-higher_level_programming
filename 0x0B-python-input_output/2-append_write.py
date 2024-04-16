#!/usr/bin/python3
"""This module defines a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Function appends to a text file (UTF8)

    Args:
        filename: name of file, type(string)
        text: text to be appended to the file, type(string)

    Return:
        number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        word_count = f.write(text)
    return word_count
