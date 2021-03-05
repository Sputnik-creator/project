# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def high(a):
    max_ = 0
    for n in a:
        if n > max_:
            max_ = n
    return max_


my_dict = dict()
for i in array:
    quantity = 0
    for el in array:
        if i == el:
            quantity += 1
    my_dict.update({i: quantity})
print(my_dict)
b = high(my_dict.values())
print(b)
