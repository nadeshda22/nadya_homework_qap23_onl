"""1. Напиши функцию copy_file(source: str, destination: str) -> bool
которая читает содержимое файла source и записывает его в destination. Возвращает True если успешно.
Проверь что файл-копия создался.
"""

import os
from datetime import datetime
from file_utils import read_lines, write_lines, count_words

source = "source.txt"
destination = "destination.txt"


def copy_file(source: str, destination: str) -> bool:
    try:
        with open(source, "r") as file:
            copy = file.read()

        with open(destination, "w") as file:
            file.write(copy)

        return True
    except FileNotFoundError:
        return False


print(copy_file(source, destination))
"""
2. Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
Анна,85
Иван,72
Петр,91
Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' если оценка >= 90,
 'хорошо' если >= 75, иначе 'удовлетворительно'. Сохрани результат в новый файл grades_with_status.txt.
"""

print("=" * 50)


def get_status(grade: int) -> str:
    if 100 >= grade >= 90:
        return "отлично"
    elif 90 >= grade >= 75:
        return "хорошо"
    else:
        return "удовлетворительно"


with open("grades.txt", "r") as file:
    lines = file.readlines()

with open("grades_with_status.txt", "w") as out_file:
    for line in lines:
        line = line.strip()
        if line:
            name, grade = line.split(",")
            status = get_status(int(grade))
            out_file.write(f"{name},{grade},{status}\n")

"""
3. Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет.
"""

print("=" * 50)


def age_calculator(birth_date: str) -> int:
    current_date = datetime.now()
    birth_date_obj = datetime.strptime(birth_date, "%d/%m/%Y")

    age = current_date.year - birth_date_obj.year

    if (current_date.month, current_date.day) < (
        birth_date_obj.month,
        birth_date_obj.day,
    ):
        age -= 1

    return age


birth_date = input("Введите дату рождения(dd/mm/yyyy): ")
print(age_calculator(birth_date))

"""
4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

def read_lines(filename): ...
def write_lines(filename, lines): ...
def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь.
В main.py импортируй и протестируй все три.
"""

print("=" * 50)


def main():
    test_file = "test.txt"
    test_data = [
        "Привет мир!",
        "Это тестовый файл.",
        "Привет снова, мир!",
        "Тест тест тест.",
        "Python программирование это весело!",
        "Весело весело весело!",
    ]

    print("\n1. Тестирование write_lines (запись в файл):")
    write_lines(test_file, test_data)
    print(f"   ✓ Файл '{test_file}' успешно создан")
    print(f"   ✓ Записано {len(test_data)} строк")

    print("\n2. Тестирование read_lines (чтение из файла):")
    lines = read_lines(test_file)
    print(f"   ✓ Прочитано {len(lines)} строк:")
    for i, line in enumerate(lines[:3], 1):
        print(f"     {i}. {line}")
    if len(lines) > 3:
        print(f"     ... и еще {len(lines) - 3} строк")

    print("\n3. Тестирование count_words (подсчет слов):")
    word_counts = count_words(test_file)
    print(f"   ✓ Найдено {len(word_counts)} уникальных слов")
    print("   ✓ Топ-5 самых частых слов:")

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:5]:
        print(f"     • '{word}': {count} раз(а)")

    print("\n4. Тестирование обработки ошибок:")
    try:
        read_lines("несуществующий_файл.txt")
    except FileNotFoundError as e:
        print(f"   ✓ Ошибка обработана: {e}")

    os.remove(test_file)
    print(f"\n✓ Тестовый файл '{test_file}' удален")


"""5. Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password). Вложенная принимает пароль и возвращает True если совпадает, иначе False. Внешняя переменная с паролем не должна быть доступна снаружи:"""


def password_checker(correct_password):

    def check(password):
        return password == correct_password

    return check


checker = password_checker(input("Введите секретное слово"))
answer = input("Введите повторно")

print(checker(answer))
