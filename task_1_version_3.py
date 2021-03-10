# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.
# https://drive.google.com/file/d/1fPzMmafxXRUwmLjNvr-bi3zo0VNUHJAW/view?usp=sharing

import timeit
import cProfile


def func_3(n):
    while True:
        res = 0
        if n < len(row):
            for i in row:
                res = res + i
            return res
        row.append(row[-1] * -0.5)


row = [1, -0.5, 0.25, -0.125]

print(timeit.timeit('func_3(1_000)', number=100, globals=globals()))  # 0.007774189000000001
print(timeit.timeit('func_3(2_000)', number=100, globals=globals()))  # 0.014446512999999994
print(timeit.timeit('func_3(4_000)', number=100, globals=globals()))  # 0.027283481
print(timeit.timeit('func_3(8_000)', number=100, globals=globals()))  # 0.05322144699999999
print(timeit.timeit('func_3(16_000)', number=100, globals=globals()))  # 0.10716569599999998

cProfile.run('func_3(125_000)')
cProfile.run('func_3(250_000)')
cProfile.run('func_3(500_000)')
cProfile.run('func_3(1_000_000)')

'''Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.105    0.105 <string>:1(<module>)
        1    0.074    0.074    0.105    0.105 task_1_version_3.py:10(func_3)
        1    0.000    0.000    0.105    0.105 {built-in method builtins.exec}
   109001    0.017    0.000    0.017    0.000 {built-in method builtins.len}
   109000    0.015    0.000    0.015    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         250005 function calls in 0.139 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.139    0.139 <string>:1(<module>)
        1    0.095    0.095    0.139    0.139 task_1_version_3.py:10(func_3)
        1    0.000    0.000    0.139    0.139 {built-in method builtins.exec}
   125001    0.019    0.000    0.019    0.000 {built-in method builtins.len}
   125000    0.026    0.000    0.026    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         500005 function calls in 0.277 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.277    0.277 <string>:1(<module>)
        1    0.192    0.192    0.277    0.277 task_1_version_3.py:10(func_3)
        1    0.000    0.000    0.277    0.277 {built-in method builtins.exec}
   250001    0.037    0.000    0.037    0.000 {built-in method builtins.len}
   250000    0.048    0.000    0.048    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1000005 function calls in 0.717 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.717    0.717 <string>:1(<module>)
        1    0.491    0.491    0.717    0.717 task_1_version_3.py:10(func_3)
        1    0.000    0.000    0.717    0.717 {built-in method builtins.exec}
   500001    0.104    0.000    0.104    0.000 {built-in method builtins.len}
   500000    0.123    0.000    0.123    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''