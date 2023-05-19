#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set(my_list)
    summation = 0
    for i in new_list:
        summation += i

    return summation
