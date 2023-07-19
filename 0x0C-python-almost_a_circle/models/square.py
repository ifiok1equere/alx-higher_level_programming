#!/usr/bin/python3
""" This module defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class is the grandchild class which inherits
    from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - "
                "{:d}".format(self.id, self.x, self.y,
                              self.height))

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        attributes = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
