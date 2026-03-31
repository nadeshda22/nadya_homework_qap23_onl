"""4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

def read_lines(filename): ...
def write_lines(filename, lines): ...
def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь.
В main.py импортируй и протестируй все три."""

import os
from collections import Counter
from typing import List, Dict


def read_lines(filename: str) -> List[str]:

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.rstrip("\n") for line in lines]
    except IOError as e:
        raise IOError(f"Ошибка чтения файла '{filename}': {e}")


def write_lines(filename: str, lines: List[str]) -> None:

    try:
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
    except IOError as e:
        raise IOError(f"Ошибка записи '{filename}': {e}")


def count_words(filename: str) -> Dict[str, int]:

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

            words = []
            for word in content.split():
                cleaned_word = "".join(char.lower() for char in word if char.isalnum())
                if cleaned_word:
                    words.append(cleaned_word)

            return dict(Counter(words))

    except IOError as e:
        raise IOError(f"Ошибка чтения '{filename}': {e}")
