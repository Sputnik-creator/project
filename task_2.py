# Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def separator(data):
    if len(data) > 1:
        part_1 = separator(data[:len(data) // 2])
        part_2 = separator(data[len(data) // 2:])
        return merge(part_1, part_2)
    return data


def merge(list_1, list_2):
    res = []
    while len(list_1) > 0 and len(list_2) > 0:
        if list_1[0] < list_2[0]:
            res.append(list_1[0])
            list_1 = list_1[1:]
        elif list_2[0] < list_1[0]:
            res.append(list_2[0])
            list_2 = list_2[1:]
    if len(list_1) > 0:
        res += list_1
    elif len(list_2) > 0:
        res += list_2
    return res


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print(array)
print(separator(array))
