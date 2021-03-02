# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843
# https://drive.google.com/file/d/1dh81U2Qgo_HMtLvpT-7UOo3tE72wGGdX/view?usp=sharing
def func(a, b=''):
    if a // 10 == 0:
        b = b + str(a % 10)
        return b
    else:
        b = b + str(a % 10)
        return func(a // 10, b)


c = int(input('Введите целое число '))
d = func(c)
print(d)
