#!/usr/bin/python3


def remove_char_at(str, n):
    str_copy = ""
    if n <= len(str) and n >= 0:
        for char in str:
            if char != str[n]:
                str_copy += char
        return(str_copy)
    else:
        return(str)
