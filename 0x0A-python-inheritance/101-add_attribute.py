#!/usr/bin/python3
""" The module defines a function"""


def add_attribute(obj, name, value):
    """Function dtermines when an attribute can be added"""

    if obj.__class__.__name__ != "MyClass":
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
