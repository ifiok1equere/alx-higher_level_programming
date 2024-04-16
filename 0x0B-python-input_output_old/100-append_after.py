#!/usr/bin/python
""" This module inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ This function appends new_string @ the line a search_string is found
    """

    with open(filename, 'a+', encoding="utf-8") as file:
        for line in file:
            print(line)
            if search_string in line:
                file.write(new_string + "\n")
