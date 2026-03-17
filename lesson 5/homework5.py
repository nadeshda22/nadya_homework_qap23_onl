import math_utils

"""1. Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27"""

number = int(input("Введите цифру для таблицы умножения: "))
for i in range(1, 11):
    if i < 10:
        print(number * i, end=" | ")
    else:
        print(number * i)

"""2. Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»"""

name = input("Введите имя: ")
age = int(input("Введите возраст: "))

print(f"Через 10 лет тебе будет {age + 10} лет, {name}!")

"""3. Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. Затем используй
zip чтобы создать словарь {товар: цена_в_рублях}:"""

items = ["хлеб", "молоко", "кофе"]
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2


def convert_in_blr(prices):
    """
    Конвертирует цену из долларов в рубли по заданному курсу.

    Args:
        prices (float): Цена в долларах

    Returns:
        float: Цена в рублях, округленная до целого числа
    """
    return round(prices * rate)


"""Почему без функции round вывод странный? {'хлеб': 4.800000000000001, 'молоко': 6.4, 'кофе': 25.6}"""

prices_blr = list(map(convert_in_blr, prices_usd))
items_dict = dict(zip(items, prices_blr))
print(items_dict)

"""4. Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку: 'Fizz' если делится на 3, 
'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, иначе само число в виде строки. 
Вызови её для чисел от 1 до 20 через map."""


def fizzbuzz(number):
    """
    Возвращает 'Fizz', 'Buzz', 'FizzBuzz' или число в виде строки в зависимости от делимости.

    Args:
        number (int): Проверяемое число

    Returns:
        str: 'Fizz' если делится на 3, 'Buzz' если делится на 5,
             'FizzBuzz' если делится на 3 и 5, иначе число в виде строки
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


print(list(map(fizzbuzz, range(1, 20))))

"""5. Напиши функцию *args с именем my_stats которая принимает любое количество чисел и возвращает сразу три значения 
— минимум, максимум и среднее."""


def my_stats(*numbers):
    """
    Вычисляет статистические показатели для переданных чисел.

    Args:
        *numbers: Произвольное количество чисел

    Returns:
        tuple: (минимум, максимум, среднее арифметическое)
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


min_val, max_val, avg_val = my_stats(5, 8, 12, 3, 7)
print(f"Минимум: {min_val}, Максимум: {max_val}, Среднее: {avg_val}")

"""6. Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы 
и возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True. Добавь к функции docstring."""


def build_profile(**info):
    """
    Создает профиль пользователя на основе переданных данных.

    Принимает произвольные именованные аргументы и добавляет к ним
    ключ 'registered' со значением True.

    Args:
        **info: Произвольные именованные аргументы с данными пользователя

    Returns:
        dict: Словарь с данными пользователя и ключом 'registered': True
    """
    profile = dict(info)
    profile["registered"] = True
    return profile


user1 = build_profile(name="Иван", age=30, profession="разработчик")
print(user1)
user2 = build_profile(
    username="elena_dev",
    email="elena@example.com",
    years_experience=5,
    is_premium=False,
)
print(user2)
help(build_profile)

"""7. Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, cube(n) — возводит в куб, 
is_even(n) — возвращает True/False. В main.py импортируй модуль, попроси пользователя ввести число через input, 
примени все три функции и выведи результаты. Защити вызовы конструкцией if __name__ == "__main__"."""

if __name__ == "__main__":
    digits = int(input("Введите число: "))

    my_stats_1 = math_utils.square(digits)
    my_stats_2 = math_utils.cube(digits)
    my_stats_3 = math_utils.is_even(digits)

    print(f"Квадрат: {my_stats_1}")
    print(f"Куб: {my_stats_2}")
    print(f"Четное? {my_stats_3}")
