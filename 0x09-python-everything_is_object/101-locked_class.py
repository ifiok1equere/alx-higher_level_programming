#!/usr/bin/python3
"""This module defines a class"""


class LockedClass:
    """ This class defines ground rules for
    setting an attribute and raises errors when
    violated """

    def __setattr__(self, attribute, value):
        if not attribute == "first_name":
            raise AttributeError("'{}' object has no attribute \
'{}'".format(self.__class__.__name__, attribute))
