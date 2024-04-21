#!/usr/bin/python3
"""THis module defines a model blueprint"""
import json


class Base():
    """This class define a blueprint for creating objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization Method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
