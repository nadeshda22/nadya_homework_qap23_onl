"""
1. Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.
"""

from typing import List, Callable, Any, TypeVar, Iterator, Optional, Union

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers: List[int] = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

print('-' * 50)
"""
2. Напишите функцию apply_operations(numbers, *operations), которая принимает список чисел 
и произвольное количество lambda-функций, последовательно применяя каждую ко всему списку.
"""

def apply_operations(
    numbers: List[float | int], *operations: Callable[[float | int], float | int]
) -> List[float | int]:
    result: List[float | int] = numbers.copy()
    for operation in operations:
        result = list(map(operation, result))
    return result


numbers: List[int] = [1, 2, 3, 4, 5]
result: List[float | int] = apply_operations(
    numbers, lambda x: x * 2, lambda x: x + 1, lambda x: x**2
)
print(result)

print('-' * 50)
"""
3. Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера 
и поочередно их выдает. Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].
"""

T = TypeVar("T")


def chunked(lst: List[T], size: int) -> Iterator[List[T]]:
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


for chunk in chunked([1, 2, 3, 4, 5], 2):
    print(chunk)

print('-' * 50)
"""
4. Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20.
"""

def prime_numbers() -> Iterator[int]:

    yield 2
    primes: List[int] = [2]
    n: int = 3
    while True:
        is_prime: bool = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 2


gen: Iterator[int] = prime_numbers()
first_20: List[int] = [next(gen) for _ in range(20)]
print(first_20)

print('-' * 50)
"""
5. Напишите функцию safe_convert(value, type_func), которая пытается преобразовать value 
с помощью переданной функции (например, int, float). При ошибке возвращает None.
"""

T = TypeVar("T")


def safe_convert(value: Any, type_func: Callable[[Any], T]) -> Optional[T]:

    try:
        return type_func(value)
    except (ValueError, TypeError):
        return None


print(safe_convert("123", int))
print(safe_convert("abc", int))
print(safe_convert("3.14", float))
print(safe_convert([1, 2], int))

print('-' * 50)
"""
6. Создайте собственный класс исключения NegativeNumberError. Напишите функцию sqrt_safe(n), которая считает 
квадратный корень из числа, но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением.
"""


class NegativeNumberError(Exception):
    def __init__(
        self,
        message: str = "Невозможно вычислить квадратный корень из отрицательного числа",
    ) -> None:
        self.message: str = message
        super().__init__(self.message)


def sqrt_safe(n: Union[int, float]) -> float:

    try:
        if n < 0:
            raise NegativeNumberError(
                f"Число {n} отрицательное. Квадратный корень из отрицательного числа не определен."
            )
        return n**0.5
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")
        raise


try:
    print(sqrt_safe(16))
    print(sqrt_safe(-5))
except NegativeNumberError:
    pass

print('-' * 50)
"""
7. Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/"). 
Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.
"""

Number = Union[int, float]


def calculator(a: Number, b: Number, op: str) -> Optional[Number]:
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Аргументы должны быть числами")

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            return a / b
        else:
            raise ValueError(
                f"Неизвестная операция: {op}. Доступные операции: +, -, *, /"
            )

    except (TypeError, ZeroDivisionError, ValueError) as e:
        print(f"Ошибка: {e}")
        return None


number1 = int(input("Введите первое число:"))
number2 = int(input("Введите второе число:"))
operator = input("Введите оператор")

print(calculator(number1, number2, operator))
print('-' * 50)