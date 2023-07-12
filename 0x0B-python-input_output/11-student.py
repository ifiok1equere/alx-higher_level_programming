#!/usr/bin/python3
""" My class module
"""


class Student:
    """ My class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            attr = {}
            list_dict = self.__dict__
            for key, value in list_dict.items():
                if key in attrs:
                    attr[key] = value
            return attr
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json
