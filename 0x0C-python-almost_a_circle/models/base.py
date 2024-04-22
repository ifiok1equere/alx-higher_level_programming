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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json string to a file"""

        filename = "{:s}.json".format(cls.__name__)

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("[]")
        else:
            with open(filename, "w", encoding="utf-8") as file:
                new_list = []
                for instance in list_objs:
                    new_list.append(instance.to_dictionary())
                json.dump(new_list, file)            
