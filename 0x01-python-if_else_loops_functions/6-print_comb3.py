#!/usr/bin/python3

for i in range(9):
    for j in range(i + 1, 10):
        if j < 10:
            print("{:d}{:d}, ".format(i, j) if i < 8 else "{}{}".format(i, j),
                  end="" if i < 8 else "\n")
