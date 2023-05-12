#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_copy = my_list.copy()
    new_copy[idx] = element
    return (new_copy)
