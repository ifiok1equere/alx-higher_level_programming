#!/usr/bin/python3
'''
This is a module that provides a class definition for a square.
'''


class Square:
    ''' The class defines a square. '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        The __init__ method creates a private attribute \
        called size and is instantiated to a variable called size.

        Args:
            size (int): a critical parameter of a square
        '''
        try:
            self.size = size
            self.position = position
        except:
            #print(e)
            self.position = (0, 0)

    def area(self):
        '''
        The area method is a public instance method that computes the area of a
        square and returns the result.

        Note:
            Reference made to the private instance attribute size for function
            argument.
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
        This method is a public instance method that prints to stdout the
        square defined by size with the character '#'.

        Note:
            Reference made to the private instance attribute size for function
            argument.
        '''
        if (self.__size == 0) or (self.__position == (0, 0)):
            print('')
        else:
            j = 0
            if self.__position[1] > 0:
                print()
            for i in range(self.__size):
                while j < self.__position[0]:
                    print(' ', end="")
                    j += 1
                for k in range(self.__size):
                    print('#', end="")
                j = 0
                print()

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''
        The setter method is a private instance method that ensures the size of
        the square is set to the value size and cannot be changed.

        Note:
            Reference made to the private instance attribute size for function
            argument.
        '''
        if (type(value) is not tuple) or \
                (len(value) != 2) or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
