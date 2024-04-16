#!/usr/bin/python3
""" This module defines a function that works on an obj """


def class_to_json(obj):
    """
    This function builds a dictionary from an object """
    return sorted(obj.__dict__)
