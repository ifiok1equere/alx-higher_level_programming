#!/usr/bin/python3
"""This Class inherits from list"""


class MyList(list):
    """
    This class inherits from list.

    Args:
        obj: type(list)

    Return:
        Instance of the class List
    """

    def print_sorted(self):
        """This method prints a sorted list"""

        self.sort()
        print(self)
