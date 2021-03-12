from collections import defaultdict

n = int(input('Введите количество предприятий '))
a = defaultdict(list)
average_income = 0
list_1 = []
list_2 = []
for numb in range(1, n+1):
    name = input(f'Введите название {numb}-го предприятия ')
    for i in range(1, 5):
        income = int(input(f'Введите доход предприятия {name} за {i}-ый квартал '))
        a[name].append(income)
    average_income = average_income + sum(a[name])/n
for name in a:
    if sum(a[name]) > average_income:
        list_1.append(name)
    else:
        list_2.append(name)
print(f'Средняя прибыль для предприятий составляет {average_income}')
print(f'Предприятия с прибылью выше среднего {list_1}')
print(f'Предприятия с прибылью ниже среднего {list_2}')
