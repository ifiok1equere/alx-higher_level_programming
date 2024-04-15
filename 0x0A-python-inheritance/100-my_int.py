#!/usr/bin/python3
"""This a class called MyInt"""


class MyInt(int):
    """This class inherits from the int class"""

    def __eq__(self, other): 
        """Overide __eq__ method to invert equality value"""

        return False
    
    def __ne__(self, other): 
        """Overide __ne__ method to invert inequality value"""

        return True
