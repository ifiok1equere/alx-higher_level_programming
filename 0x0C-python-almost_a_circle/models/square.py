#!/usr/bin/python3
""" models/square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a blueprint for creating Square Class objects"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization Method"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The unofficial representation of the square object"""

        cls_name = self.__class__.__name__
        id_ = self.id
        x = self.x
        y = self.y
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                cls_name, id_, x, y, self.width
                )
