# Вводятся три разных числа.
# Найти, какое из них является средним
# (больше одного, но меньше другого).
# https://drive.google.com/file/d/1wYPYIR-89R6HnizMw04Lp6eJn21PTMbK/view?usp=sharing
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третье число"))
if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
else:
    if b < c:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)
