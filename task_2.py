#  Посчитать четные и нечетные цифры введенного натурального
#  числа. Например, если введено число 34560, в нем 3 четные
#  цифры (4, 6 и 0) и 2 нечетные (3 и 5)
# https://drive.google.com/file/d/1xIh6ov5hV-82p_RuR1Dx20RaEtTXrWm7/view?usp=sharing

def calculator(a, b=0, c=0):
    if (a % 10) % 2 == 0 and a // 10 == 0:
        b += 1
        return f'Четных цифр {b}, нечтных {c}'
    elif (a % 10) % 2 != 0 and a // 10 == 0:
        c += 1
        return f'Четных цифр {b}, нечтных {c}'
    elif (a % 10) % 2 == 0:
        return calculator(a // 10, b + 1, c)
    else:
        return calculator(a // 10, b, c + 1)


f = int(input('Введите целое натуральное число'))
d = calculator(f)
print(d)
