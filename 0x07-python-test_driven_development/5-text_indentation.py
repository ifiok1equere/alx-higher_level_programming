#!/usr/bin/python3
"""
This module defines a function that prints a text.
This function does this printing according to
some rules detailed in the function's doc string.
"""


def text_indentation(text):
    """ Function that prints a text with
        2 new lines after each of the characters: ., and ?
        Args: text (string) """

    if not isinstance(text, str):
        raise TypeError(
                "text must be a string"
                )

    delimiters = ('.', '?', ':')

    for delimiter in delimiters:
        text = text.replace(delimiter, delimiter + '\n')

    lines = text.split('\n')
    for line in lines:
        if line.strip() != "":
            if "." in line or "?" in line or ":" in line:
                print(line.strip())
                print()
            else:
                print(line.strip(), end="")
