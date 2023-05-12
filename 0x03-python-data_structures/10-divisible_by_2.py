#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    bol_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bol_list.append(True)
        else:
            bol_list.append(False)
    return (bol_list)
