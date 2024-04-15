#!/usr/bin/python3
"""This is a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This square class inherits from Rectangle"""

    def __init__(self, size):
        """Initialization method"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        """Computes area of the square"""

        return self._size * self._size
