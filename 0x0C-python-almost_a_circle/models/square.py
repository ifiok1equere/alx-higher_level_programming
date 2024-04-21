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

    @property
    def size(self):
        """Size Getter Method"""

        return self.width

    @size.setter
    def size(self, size):
        """Size Setter Method"""

        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """This method updates the attributes of the square class"""

        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
