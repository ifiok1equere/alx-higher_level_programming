#!/usr/bin/python3
"""This module defines a class"""


class Student:
    """This class defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialization Method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method serializes an object

        Args:
            self: reference to the object instance

        Return:
            dictionary description of self
        """

        return self.__dict__
