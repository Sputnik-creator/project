# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.
# https://drive.google.com/file/d/1XgVE8Xij-pOEymgZZsO84XBvNpFaaJZb/view?usp=sharing

a = int(input("Введите любое трехзначное целое число "))
b = a % 10
c = (a % 100 - b) / 10
d = a // 100
f = d + b + c
g = d * b * c
print(f"Сумма чисел равна {f}."
      f"Произведение чисел равно {g}")
