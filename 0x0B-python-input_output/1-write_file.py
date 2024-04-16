#!/usr/bin/python3
"""This module defines a function that writes to a text file"""


def write_file(filename="", text=""):
    """Function writes to a text file (UTF8)

    Args:
        filename: name of file, type(string)
        text: text to be written into the file, type(string)

    Return:
        number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        word_count = f.write(text)
    return word_count
