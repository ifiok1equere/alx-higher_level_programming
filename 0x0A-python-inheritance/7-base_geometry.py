#!/usr/bin/python3

""" This is an Empty Class"""


class BaseGeometry():
    """
    Empty Class.
    """

    def area(self):
        """Computes area of a polygon"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values passed"""

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
