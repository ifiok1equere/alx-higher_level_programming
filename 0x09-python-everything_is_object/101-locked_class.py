#!/usr/bin/python3
"""This module defines a class"""


class LockedClass(object):
    """ This class defines ground rules for
    setting an attribute and raises errors when
    violated """

    def __setattr__(self, attribute, value):
        if not attribute == "first_name":
            raise AttributeError(f"'{self.__class__.__name__}' \
                    object has no attribute '{attribute}'")
        else:
            object.__setattr__(self, attribute, value)
