# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.
# https://drive.google.com/file/d/1fPzMmafxXRUwmLjNvr-bi3zo0VNUHJAW/view?usp=sharing

import timeit
import cProfile


def append_(n):
    if n >= len(row):
        row.append(row[-1] * -0.5)
        return append_(n)
    return sum(row[:n])


row = [1, -0.5, 0.25, -0.125]
print(append_(7))

print(timeit.timeit('append_(125)', number=100, globals=globals()))  # 0.0006612090000000029
print(timeit.timeit('append_(250)', number=100, globals=globals()))  # 0.0007889229999999969
print(timeit.timeit('append_(500)', number=100, globals=globals()))  # 0.0014994950000000035
print(timeit.timeit('append_(2000)', number=100, globals=globals()))  # 0.002640759999999999

cProfile.run('append_(125)')
cProfile.run('append_(250)')
cProfile.run('append_(500)')
cProfile.run('append_(1_000)')

'''   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_2.py:10(append_)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_2.py:10(append_)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_2.py:10(append_)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_version_2.py:10(append_)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''