#!/usr/bin/python3
"""This module defines a class"""


class Student:
    """This class defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialization Method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method serializes an object

        Args:
            self: reference to the object instance

        Return:
            dictionary description of self
        """
        new_dict = {}

        if attrs is not None:
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Retrieves a dictionary representation of a Student instance

        Args:
            self: reference to object instnace
            json: dictionary description of self

        Return:
            Self instance and all its attributes
        """

        for key, value in json.items():
            setattr(self, key, value)
