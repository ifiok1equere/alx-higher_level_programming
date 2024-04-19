#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(10, 7, 2, 8)
    dictionary_1 = r1.to_dictionary()
    dictionary_2 = r2.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary_1, dictionary_2])
    print(dictionary_1)
    print(type(dictionary_1))
    print(dictionary_2)
    print(type(dictionary_2))
    print(json_dictionary)
    print(type(json_dictionary))
