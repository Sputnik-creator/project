# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
array = [2, 3, 4, 5, 6, 7, 8, 9]
for el in array:
    quantity = 0
    pos = 0
    for i in range(2, 100):
        if i % el == 0:
            quantity += 1
    print(f'{el} - > {quantity}')
