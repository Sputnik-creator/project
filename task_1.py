# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib


def func(string):
    substring = set()
    for i in range(len(string)-1):
        substring.add(hashlib.md5(string[i+1].encode('utf-8')).hexdigest())
        substring.add(hashlib.md5(string[i:len(string)-1].encode('utf-8')).hexdigest())
        substring.add(hashlib.md5(string[i+1:len(string)].encode('utf-8')).hexdigest())
        substring.add(hashlib.md5(string[:i+1].encode('utf-8')).hexdigest())
    return substring


str_ = input('Введите строку: ')
print(f'В строке {len(func(str_))} подстрок')
