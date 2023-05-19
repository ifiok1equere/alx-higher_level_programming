#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or roman_string == "":
        return 0
    dict_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) == 1:
        return dict_1[roman_string]
    total = dict_1[roman_string[0]]
    for i in range(1, len(roman_string)):
        for key, value in dict_1.items():
            if key == roman_string[i]:
                if dict_1[key] <= dict_1[roman_string[i - 1]]:
                    total += value
                    break
                else:
                    x = 2 * dict_1[roman_string[i - 1]]
                    total = total + dict_1[key] - x
                    break
    return total
