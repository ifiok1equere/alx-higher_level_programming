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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        The area method is a public instance method that computes the area of a
        square and returns the result.

        Note:
            Reference made to the private instance attribute size for function
            argument.
        '''
        return self.__size * self.__size
