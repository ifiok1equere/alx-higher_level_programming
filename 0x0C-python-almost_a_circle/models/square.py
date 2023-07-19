#!/usr/bin/python3
""" This module defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class is the grandchild class which inherits
    from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ This method initializes an instance of the square object """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The method is an overridding __str__
        function for the square class
        """
        return ("[Square] ({:d}) {:d}/{:d} - "
                "{:d}".format(self.id, self.x, self.y,
                              self.height))

    @property
    def size(self):
        """ This is the size getter method """
        return self.height

    @size.setter
    def size(self, value):
        """ This is the size setter method """
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        This is a method that updates and
        sets the attribute of a class instance
        """
        attributes = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This method return a dictionary
        representation of a class instance
        """
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
