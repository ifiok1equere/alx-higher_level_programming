'''

def number_test(num):
    return num % 2 == 0


def receive(func, mylist=[]):
    odd_list = []
    for num in mylist:
        if func(num) is False:
            odd_list.append(num)

    return odd_list

x = receive(number_test, [2, 5, 7, 8, 3])
print(x)
'''

import random
x = []
for i in range(1, 101):
    x.append(random.choice(range(1, 1001)))
print(list(filter(lambda x: x % 9 == 0, x)))
