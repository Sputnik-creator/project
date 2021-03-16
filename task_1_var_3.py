# Определить, какое число в массиве встречается чаще всего.
import random
import sys
from collections import Counter


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


def conclusion(dict_):
    for key, values in dict_:
        print(f'Число {key} встречается {values} раз')
        break


SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count = Counter(array)
print(count)
b = count.most_common(1)
c = conclusion(b)
print(f'Объем памяти в данной прграмме составляет {(show(array) + show(count) + show(b) + show(c)) / 1024:.2f} Kb')
# Объем памяти в данной прграмме составляет 4.66 Kb
