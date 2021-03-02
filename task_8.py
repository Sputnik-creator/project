# Посчитать, сколько раз встречается определенная цифра в
# введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом
# с клавиатуры.
# https://drive.google.com/file/d/1R26l4gW-xoNvKREkArfRCx6Vui-__cDE/view?usp=sharing
def func(a, b, c=0):
    if b // 10 == 0 and b % 10 == a:
        c += 1
        return c
    elif b // 10 == 0 and b % 10 != a:
        return c
    elif b % 10 == a:
        c += 1
        return func(a, b // 10, c)
    else:
        return func(a, b // 10, c)


length = int(input('Введите длинну числового ряда '))
search = int(input('Введите искомое число '))
res = 0
i = 1
while length > 0:
    argument = int(input(f'Введите {i}-е число '))
    length -= 1
    i += 1
    res = res + func(search, argument)
print(f'Количество искомых цыфр равно {res}')
