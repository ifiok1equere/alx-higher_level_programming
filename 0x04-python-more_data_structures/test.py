'''
def intersection(set_1={}, set_2={}):
    list_1 = []
    for num in set_1:
        for item in set_2:
            if item == num:
                list_1.append(num)
    return list_1
def intersection(set_1, set_2):
'''
x = "ifiok"
y = "equere"
dictionary_1 = {(x, y): 'arnold', 12: 'python', 'name': 'Henok'}
print(dictionary_1[12])
print(dictionary_1['name'])
