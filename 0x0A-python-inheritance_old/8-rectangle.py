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
