#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) - 32) if ord(char) >= 97 and
              ord(char) <= 122 else "{:s}".format(char), end="")
    else:
        print("{:s}".format("\n"), end="")

