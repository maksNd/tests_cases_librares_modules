# видео https://www.youtube.com/watch?v=pXgWcTwECAg&t=17s

import re
"""
Методы регулярных выражений в python:
match ищет по заданному шаблону только в начале строки
search - ищет во всей строке, но только первое совпадение
findall - ищет все элементы которые попадают под наш шаблон, возвращает список со всеми совпадениями
sub - ищет подстроку и заменяет ее
"""

text_example = 'кот собака котейка собачник прогулка Иванова А.А. Петров М Колпаков КС Ко1товМ'

"""
match ищет по заданному шаблону только в начале строки
"""
result_1 = re.match(r'кот', text_example)
print(result_1)
print(result_1.group())  # распечатает найденную подстроку

result_2 = re.match(r'соб', text_example)
print(result_2)
# print(result_2.group())  # выдаст ошибку, т.к. match ищет только в начале

"""
search - ищет во всей строке, но только первое совпадение
"""
result_3 = re.search(r'собака', text_example)
print(result_3)
print(result_3.group())

"""
findall - ищет все элементы которые попадают под наш шаблон, возвращает список со всеми совпадениями
"""
result_4 = re.findall(r'соб', text_example)
print(result_4)

"""
sub - ищет подстроку и заменяет ее
"""
result_5 = re.sub('прогулка', 'отпуск', text_example)  # не меняет исходную строку
print(result_5)

"""
пример паттерна для поиска имен
"""
pattern = r'[А-Я][а-я]+\ ?[А-Я]\.?[А-Я]?\.?'
print(re.findall(pattern, text_example))
