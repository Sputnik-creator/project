# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.
# https://drive.google.com/file/d/1fPzMmafxXRUwmLjNvr-bi3zo0VNUHJAW/view?usp=sharing

import timeit
import cProfile


def func_1(n):
    i = 1
    b = 1
    c = 1
    while i < n:
        c = c + b * -0.5
        b = b * -0.5
        i += 1
    return c


print(timeit.timeit('func_1(1000)', number=100, globals=globals()))  # 0.032061396
print(timeit.timeit('func_1(2000)', number=100, globals=globals()))  # 0.057102654
print(timeit.timeit('func_1(4000)', number=100, globals=globals()))  # 0.11715131200000001
print(timeit.timeit('func_1(8000)', number=100, globals=globals()))  # 0.22081214600000001
print(timeit.timeit('func_1(16000)', number=100, globals=globals()))  # 0.438270241

cProfile.run('func_1(1_000)')
cProfile.run('func_1(10_000)')
cProfile.run('func_1(100_000)')
cProfile.run('func_1(1_000_000)')


'''4 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:10(func_1)
        1    0.001    0.001    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.004    0.004    0.004    0.004 task_4.py:10(func_1)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.028 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.028    0.028 <string>:1(<module>)
        1    0.028    0.028    0.028    0.028 task_4.py:10(func_1)
        1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.306 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.305    0.305 <string>:1(<module>)
        1    0.305    0.305    0.305    0.305 task_4.py:10(func_1)
        1    0.000    0.000    0.306    0.306 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''
