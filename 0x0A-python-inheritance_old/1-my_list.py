#!/usr/bin/python3
"""This module defines a class inheritance"""


class MyList(list):
    """ This class inherits from list """

    def print_sorted(self):
        """This method prints a sorted list."""

        new_list = sorted(self)
        print(new_list)
