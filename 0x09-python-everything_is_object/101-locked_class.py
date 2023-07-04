#!/usr/bin/python3
class LockedClass(object):
    def __setattr__(self, attribute, value):
        if not attribute == "first_name":
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attribute}'")
        else:
            object.__setattr__(self, attribute, value)
