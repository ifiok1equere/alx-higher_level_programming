#!/usr/bin/python3
"""This module defines a class"""


class LockedClass(object):
    """ This class defines ground rules for
    setting an attribute and raises errors when
    violated """

    def __setattr__(self, attribute, value):
        if not attribute == "first_name" and \
                isinstance(attribute, str):
            raise AttributeError("'{}' object has no attribute \
'{}'".format(self.__class__.__name__, attribute))
        else:
            object.__setattr__(self, attribute, value)
