#!/usr/bin/python3
'''
This is a module that provides a class definition for a node.
'''


class Node:
    ''' The class defines a Node. '''
    def __init__(self, data, next_node=None):
        '''
        The __init__ method creates a private attribute
        called data and is instantiated to a variable called data.

        Args:
            data (int): the data part of the node
            next_node (int): used to return the next node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        '''
        The setter method is a private instance method that ensures the data of
        the Node is set to the value data and cannot be changed.
        '''
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        The setter method is a private instance method that ensures the size of
        the square is set to the value size and cannot be changed.
        '''
        if ((value is not None) and (type(value) is not Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''
    The __init__ method creates a private attribute
    called head and is instantiated to a value None.

    Args:
        None
    '''
    def __init__(self):
        self.__head = None

    def __str__(self):
        ptr = self.__head
        val = ''
        while ptr is not None:
            if ptr.next_node is not None:
                val += str(ptr.data) + '\n'
            else:
                val += str(ptr.data)
            ptr = ptr.next_node
        return val

    def sorted_insert(self, value):
        new_node = Node(value)
        current = self.__head
        previous = self.__head
        if self.__head is None:
            self.__head = new_node
        else:
            if new_node.data < current.data:
                new_node.next_node = current
                self.__head = new_node
            else:
                while (current and (current.data < value)):
                    previous = current
                    current = current.next_node
                if current is None:
                    previous.next_node = new_node
                else:
                    new_node.next_node = current
                    previous.next_node = new_node
