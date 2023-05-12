#!/usr/bin/python3.8.5


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for sub_list in matrix:
            for i in range(len(sub_list)):
                if i < len(sub_list) - 1:
                    print("{:d} ".format(sub_list[i]), end="")
                else:
                    print("{:d}".format(sub_list[i]))
