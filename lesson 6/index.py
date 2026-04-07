# """
# Напиши функцию make_multiplier(n) которая возвращает вложенную функцию.
# Вложенная функция принимает число x и возвращает x * n. Создай умножитель на 3 и на 5, вызови каждый с числом 10:
# """
#
# from typing import Callable
import os

from file_utils import read_lines, write_lines, count_words
#
# def make_multiplier(number: int) -> Callable:
#     def funck(number1: int) -> int:
#         return number1 * number
#
#     return funck
#
#
# in_3 = make_multiplier(3)
# in_5 = make_multiplier(5)
# print(in_3(10), in_5(10))

print("=" * 50)

"""
Напиши функцию greet_user(greeting) которая возвращает вложенную функцию say(name). Вложенная выводит f'{greeting}, {name}!'.
Создай два разных приветствия и вызови их:
"""
import datetime


# def greet_user(greeting):
#     def say(name):
#         return (f'{greeting}, {name}')
#     return say
#
# hello_name = greet_user('Привет')
#
# print(hello_name(name = input('Введите имя: ')))

print("=" * 50)

"""Создай файл students.txt и запиши в него через with open список из 5 студентов — каждый на новой строке. 
Затем открой файл на чтение и выведи только те строки, длина которых больше 5 символов.
"""
# name = ['Надя','Яна','Матвей','Алексей','Стас']
#
# with open('students.txt', 'w') as file:
#     for student in name:
#         file.write(student + '\n')
#
# with open('students.txt', 'r') as file:
#     for line in file:
#         student = line.strip()
#         if len(student) > 5:
#             print(student)

print("=" * 50)

"""Напиши функцию days_until_new_year() -> int которая возвращает количество дней до нового года от сегодняшней даты. 
Используй datetime.datetime.now() и аннотируй типы"""


def days_until_new_year(year: int) -> int:
    current_data = datetime.datetime.now()
    new_year = datetime.datetime(year=year, month=1, day=1)
    return (new_year - current_data).days


print(days_until_new_year(2100))
