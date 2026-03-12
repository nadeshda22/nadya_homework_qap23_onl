from collections import Counter

print("Привести к целому типу -1.6, 2.99")
number1 = 1.6
number2 = 2.99

print(number1, number2)
print(int(number1), int(number2))

print("-" * 40)
print('Заменить символ "#" на символ "/" в строке "www.my_site.com#about"')
url = "www.my_site.com#about"

print(url)
print(url.replace("#", "/"))

print("-" * 40)
print("Напишите программу, которая добавляет 'ing' к слову 'stroka'")
word = "stroka"
word1 = "me"

print(word)
print(word1)
print(word + word1)

print("-" * 40)
print('В строке "Ivanov Ivan" поменяйте местами слова => "Ivan Ivanov"')
full_name = "Yanushevskaya Nadya"
name = full_name.split()

print(name[::-1])

print("-" * 40)
print("Напишите программу которая удаляет пробел в начале, в конце строки")
text = "1        hello       "

print(text)
print(text.lstrip())
print(text.rstrip())
print(text.strip())

print("-" * 40)
print(
    "Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество "
    "учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.)."
)
school = {
    "1a": 1,
    "2a": 2,
    "3a": 3,
    "4a": 4,
    "5a": 5,
    "6a": 6,
    "7a": 7,
    "8a": 8,
    "9a": 9,
    "10a": 10,
}

print(school)
print("Создайте список и извлеките из него списка второй элемент.")
print(list(school.items())[1])

print("-" * 40)

# full_name = 'Yanushevskaya Nadya'
# text = '1        hello       '
print("Вывести входит ли строка1 в строку2")
print(full_name)
print(text)

if full_name in text:
    print("true")
else:
    print("false")

print("-" * 40)

print("Вывести нужные символы")
text = "My name is Agent Smith"
print(text[1], text[3:16:3])

print("-" * 40)

print("Вывести уникальный элемент")

set = [1, 5, 2, 9, 2, 9, 1]
counts = Counter(set)

unique_ones = [item for item, count in counts.items() if count == 1]
print(unique_ones)
