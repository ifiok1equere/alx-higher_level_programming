#!/usr/bin/python3
"""
This module defines a printing function.
The function prints a name in a restricted
format.
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints a name in the format:
    My name is <first name> <last name>.
    Args: String: The first and second argument. """

    if not isinstance(first_name, str):
        raise TypeError(
                "first_name must be a string"
                )
    if not isinstance(last_name, str):
        raise TypeError(
                "last_name must be a string"
                )
    if first_name is None:
        raise TypeError(
                "first_name must be a string"
                )

    print("My name is {:s} {:s}".format(first_name, last_name))
