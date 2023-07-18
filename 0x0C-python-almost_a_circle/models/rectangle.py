#!/usr/bin/python3
""" This module defines a Rectangle """
from models.base import Base


class Rectangle(Base):
    """
    This class defines a Rectangle
    inherits from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y


    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height - 1):
            print(" " * self.__x + "#" * self.__width)
        print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - "
                "{:d}/{:d}".format(self.id, self.__x, self.__y,
                                   self.__width, self.__height))

    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
