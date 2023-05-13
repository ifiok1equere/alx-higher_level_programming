#!/usr/bin/python3
"""
  Prints all integers of a list, in reverse order.

  Args:
    my_list: A list of integers.

  Returns:
    None.
  """
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
