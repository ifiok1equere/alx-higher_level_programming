#!/usr/bin/python3
import magic_calculation_102


def magic_calculation(a, b):
    __import__('magic_calculation_102').add
    __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return(c)
    else:
        return(sub(a, b))
