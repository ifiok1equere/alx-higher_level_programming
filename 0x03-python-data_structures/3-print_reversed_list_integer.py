#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    '#for i in range(1, 6):'
    '#print(-i)'
    for i in range(1, len(my_list) + 1):
        print("{:d}".format(my_list[-i]))
