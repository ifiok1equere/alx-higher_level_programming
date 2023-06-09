#!/usr/bin/python3
""" This module defines a class with inheritance """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class is a class with inheritance
    from another class BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return("[Rectangle] {:s}/{:s}\
                ".format(str(self.__width), str(self.__height)))

    def print():
        print("[Rectangle] {:s}/{:s}\
                ".format(str(self.__width), str(self.__height)))
