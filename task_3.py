# Массив размером 2m + 1, где m — натуральное число, заполнен
# случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не
# рассматривался на уроках (сортировка слиянием также недопустима).
import random


def sorting(data):
    n = 0
    j = 0
    while n < len(data)-1:
        if n < 0:
            n = 0
        if data[n] > data[n+1]:
            data[n], data[n+1] = data[n+1], data[n]
            n -= 1
            print(data)
        elif data[n] <= data[n+1]:
            n += 1
            j += 1
            if n < j:
                n = j
            print(data)
    return data


size = 2 * int(input('Введите m для определения длинны масива ')) + 1
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
b = sorting(array)
print(f'Медианой в сгенерированном масиве является {b[size//2]}')
