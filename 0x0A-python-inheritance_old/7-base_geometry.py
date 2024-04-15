#!/usr/bin/python3
""" This module defines a class """


class BaseGeometry:
    """
    This class is an empty class
    but inherits an object.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(self.value, int):
            raise TypeError("{:s} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))
