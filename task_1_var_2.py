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


SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
quantity = 1
for i in range(len(array)):
    x = 0
    for y in range(i, len(array)):
        if array[i] == array[y]:
            x += 1
        if x > quantity:
            quantity = x
            max_ = array[i]
b = f'Число {max_} встречается {quantity} раз'
print(b)
print(f'Объем памяти в данной прграмме составляет '
      f'{(show(array) + show(b) + show(max_) + show(quantity) + show(i)+ show(x)+ show(y)) / 1024:.2f} Kb')
# Объем памяти в данной прграмме составляет 3.88 Kb