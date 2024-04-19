#!/usr/bin/python3
"""THis module defines a model blueprint"""

from models.base import Base


class Rectangle(Base):
    """This class defines a blueprint for creating Rectangle Class objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization Method"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width Getter Method"""

        return self.__width

    @width.setter
    def width(self, width):
        """Width Setter Method"""

        self.__width = width

    @property
    def height(self):
        """Height Getter Method"""

        return self.__height

    @height.setter
    def height(self, height):
        """Height Setter Method"""

        self.__height = height
    
    @property
    def x(self):
        """ X Co-ordinate Getter Method"""

        return self.__x

    @x.setter
    def x(self, x):
        """ X Co-ordinate Setter Method"""

        self.__x = x

    @property
    def y(self):
        """ Y Co-ordinate Getter Method"""

        return self.__y

    @y.setter
    def y(self, y):
        """ Y Co-ordinate Getter Method"""

        self.__y = y
