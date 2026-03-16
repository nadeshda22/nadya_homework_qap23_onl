"""7. Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, cube(n) — возводит в куб,
is_even(n) — возвращает True/False. В main.py импортируй модуль, попроси пользователя ввести число через input,
примени все три функции и выведи результаты. Защити вызовы конструкцией if __name__ == "__main__"."""


def square(number):
    return number * 2


def cube(number):
    return number * 3


def is_even(number):
    return number % 2 == 0
