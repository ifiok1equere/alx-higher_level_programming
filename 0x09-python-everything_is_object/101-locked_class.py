#!/usr/bin/python3
"""This module defines a class"""


class LockedClass:
    """ This class defines ground rules for
    setting an attribute and raises errors when
    violated """

    __slots__ = ["first_name"]
