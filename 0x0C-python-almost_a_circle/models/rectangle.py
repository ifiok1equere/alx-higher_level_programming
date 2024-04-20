#!/usr/bin/python3
"""THis module defines a model blueprint"""

from models.base import Base


class Rectangle(Base):
    """This class defines a blueprint for creating Rectangle Class objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization Method"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width Getter Method"""

        return self.__width

    @width.setter
    def width(self, width):
        """Width Setter Method"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Height Getter Method"""

        return self.__height

    @height.setter
    def height(self, height):
        """Height Setter Method"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """ X Co-ordinate Getter Method"""

        return self.__x

    @x.setter
    def x(self, x):
        """ X Co-ordinate Setter Method"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """ Y Co-ordinate Getter Method"""

        return self.__y

    @y.setter
    def y(self, y):
        """ Y Co-ordinate Getter Method"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """This method returns area value of instance when called"""

        return self.width * self.height

    def display(self):
        """ This method prints in stdout the Rectangle instance with the
        character # """

        for _ in range(self.height):
            print("#" * self.width)
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height - 1):
            print(" " * self.__x + "#" * self.__width)
        print(" " * self.__x + "#" * self.__width)
        """

    def __str__(self):
        """The unofficial representation of the rectangle object"""

        cls_name = self.__class__.__name__
        id_ = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                cls_name, id_, x, y, width, height
                )
