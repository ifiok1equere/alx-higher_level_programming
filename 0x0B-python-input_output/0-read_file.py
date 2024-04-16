#!/usr/bin/python3
"""This module reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Function reads a text file (UTF8) and prints it to stdout

    Args:
        filename: type(string)

    Return:
        None
    """

    with open(filename, encoding='utf-8') as f:
        file = f.read()
    print(file, end='')
