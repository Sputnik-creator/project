# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.
# https://drive.google.com/file/d/1fPzMmafxXRUwmLjNvr-bi3zo0VNUHJAW/view?usp=sharing
n = int(input('Введите количество элементов числового ряда '))
i = 1
b = 1
c = 1
while i < n:
    c = c + b * -0.5
    b = b * -0.5
    i += 1
print(c)
