# Определить, какое число в массиве встречается чаще всего.
import random
import sys


def show(obj, mem=0):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    mem = mem + sys.getsizeof(obj)
    # print(mem)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key, mem)
                mem = mem + sys.getsizeof(key)
                show(value, mem)
                mem = mem + sys.getsizeof(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item, mem)
                mem = mem + sys.getsizeof(item)
    return mem


def high(a):
    max_ = 0
    num = ''
    for key, value in a.items():
        if value > max_:
            max_ = value
            num = key
    return f'Число {num} встречается {max_} раз'


SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_dict = {}
for i in array:
    quantity = 0
    for el in array:
        if i == el:
            quantity += 1
    my_dict.update({i: quantity})

print(high(my_dict))
print(my_dict)
print(f'Объем памяти в данной прграмме составляет {(show(array) + show(my_dict)) / 1024:.2f} Kb')
# Объем памяти в данной прграмме составляет 4.52 Kb