#!/usr/bin/python3
""" This module defines a class """
import json
import os


class Base:
    """
    This class is the superclass from
    which other subsequent classes will
    inherit from.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This method initializes all instances of the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        The method returns a json string representation
        of a dictionary list
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method wites a JSON string rep of an object list to a file
        """
        obj_dict = []
        if list_objs is None:
            with open(
                    cls.__name__ + ".json", mode="w", encoding="utf-8"
                    ) as file:
                file.write()
        else:
            for obj in list_objs:
                obj_dict.append(obj.to_dictionary())
            with open(
                    cls.__name__ + ".json", mode="w", encoding="utf-8"
                    ) as file:
                file.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns an instance
        with all its attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(width=1, height=2)
        elif cls.__name__ == "Square":
            dummy = cls(size=2)
        else:
            return
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This method returns the list of instances"""
        var = []
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
            file = f.read()

        file_dict = cls.from_json_string(file)

        for dict_ in file_dict:
            var.append(cls.create(**dict_))

        return var
