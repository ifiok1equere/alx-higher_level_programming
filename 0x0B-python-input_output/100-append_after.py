#!/usr/bin/python3
"""This modeule defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: name of file
        search_string: specific string searched for
        new_string: new line to be added to file

    Return:
        None
    """

    with open(filename, 'a+', encoding="utf-8") as f:
        for line in f.readlines():
            print(line)
            if search_string in line:
                file.write(new_string + "\n")
