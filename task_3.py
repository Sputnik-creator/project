# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_ = array[0]
min_ = array[0]
for i in array:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
print(min_)
print(max_)
x = array.index(min_)
y = array.index(max_)
array[x], array[y] = array[y], array[x]
print(array)
