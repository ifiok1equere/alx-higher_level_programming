#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    score_total = 0
    weight = 0
    for i in range(len(my_list)):
        j = 0
        score_total += (my_list[i][j] * my_list[i][j + 1])
        weight += my_list[i][j + 1]
    return score_total / weight
