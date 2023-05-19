#!/usr/bin/python3


def common_elements(set_1, set_2):
    element_list = []
    for element in set_1:
        for elem in set_2:
            if elem == element:
                element_list.append(elem)
    return element_list
