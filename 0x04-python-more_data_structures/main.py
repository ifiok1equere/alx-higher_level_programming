#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_string) == 1:
        return dict_1[roman_string]
    #sum_1 = dict_1[roman_string[0]]
    sum_1 = 0
    for i in range(0, len(roman_string)):
        for key, value in dict_1.items():
            if key == roman_string[i]:
                if dict_1[roman_string[i]] < dict_1[roman_string[i + 1]]:
                    sum_1 += dict_1[roman_string[i + 1]] - value
                    if (i != len(roman_string)):
                        i += 1
                    break
                else:
                    sum_1 += value
    return sum_1

""" Roman to Integer test file
"""
roman_number = "XL"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
<3999
1. declare a dictionary that holds the roman numerals and there corresponding
values as key/value pairs. dict = {'I': 1, 'V': 5......}

2a. split argument into a list...."IX".split() = ['I', 'X']
2b. if the len(argument) == 1, return (dict[argument])

3. Declare a variable sum = dict[argument[0]]

4. Loop from index 1 of the string to the end and find a match in the
dictionary
- If we find a match, we will fetch the value and update the sum variable

'''
