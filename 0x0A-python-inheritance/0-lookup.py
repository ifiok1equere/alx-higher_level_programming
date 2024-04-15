#!/usr/bin/python3
'''
This function returns the list of available
attributes and methods of an object.
'''


def lookup(obj):
    '''
    This function returns
    the attr and meth's of
    an object passed herein
    '''

    return(dir(obj))
