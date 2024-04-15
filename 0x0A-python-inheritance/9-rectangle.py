#!/usr/bin/python3
"""This is a rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialization method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """Computes area of the rectangle"""

        return self._width * self._height

    def __str__(self):
        """Unoffical respresebtation of the object"""

        return ("[Rectangle] {:d}/{:d}".format(self._width, self._height))
