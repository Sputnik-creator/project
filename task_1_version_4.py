# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.
# https://drive.google.com/file/d/1fPzMmafxXRUwmLjNvr-bi3zo0VNUHJAW/view?usp=sharing

import timeit
import cProfile
def func_4(n):
    sector = 0.5
    sector_2 = 0.5
    if n == 1:
        return 1
    elif n == 2:
        return sector
    elif n % 2 == 0:
        for i in range(2, n, 2):
            sector = sector + (sector_2 / 2 ** i)
        return sector
    else:
        for i in range(2, n, 2):
            sector = sector + (sector_2 / 2 ** i)
        return sector + (sector_2 / 2 ** i)


print(timeit.timeit('func_4(125)', number=100, globals=globals()))  # 0.004793766000000005
print(timeit.timeit('func_4(250)', number=100, globals=globals()))  # 0.011445258
print(timeit.timeit('func_4(500)', number=100, globals=globals()))  # 0.026675259000000007
print(timeit.timeit('func_4(1000)', number=100, globals=globals()))  # 0.07388287299999999

cProfile.run('func_4(125)')
cProfile.run('func_4(250)')
cProfile.run('func_4(500)')
cProfile.run('func_4(1_000)')

'''Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_4.py:8(func_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_4.py:8(func_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_4.py:8(func_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_1_version_4.py:8(func_4)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''



