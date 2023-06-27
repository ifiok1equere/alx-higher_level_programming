#!/usr/bin/python3
'''
This is a module that provides a class definition for a square.
'''


class Square:
    ''' The class defines a square. '''
    def __init__(self, size=0):
        '''
        The __init__ method creates a private attribute \
        called size and is instantiated to a variable called size.

        Args:
            size (int): a critical parameter of a square
        '''
        self.size = size

    def area(self):
        '''
        The area method is a public instance method that computes the area of a
        square and returns the result.

        Note:
            Reference made to the private instance attribute size for function
            argument.
        '''
        return self.__size * self.__size

    def __lt__(self, object2):
        if isinstance(object2, Square):
            return self.area() < object2.area()

    def __le__(self, object2):
        if isinstance(object2, Square):
            return self.area() <= object2.area()

    def __eq__(self, object2):
        if isinstance(object2, Square):
            return self.area() == object2.area()

    def __ne__(self, object2):
        if isinstance(object2, Square):
            return self.area() != object2.area()

    def __gt__(self, object2):
        if isinstance(object2, Square):
            return self.area() > object2.area()

    def __ge__(self, object2):
        if isinstance(object2, Square):
            return self.area() >= object2.area()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''
        The setter method is a private instance method that ensures the size of
        the square is set to the value size and cannot be changed.

        Note:
            Reference made to the private instance attribute size for function
            argument.
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
