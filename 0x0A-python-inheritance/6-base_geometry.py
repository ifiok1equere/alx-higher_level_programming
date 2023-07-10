#!/usr/bin/python3
""" This module defines a class """


class BaseGeometry(object):
    """
    This class is an empty class
    but inherits an object.
    """
    def area(self):
        raise Exception("area() is not implemented")
