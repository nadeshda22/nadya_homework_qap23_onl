first_people = int(input('Введите возраст первого соседа: '))
second_people = int(input('Введите возраст второго соседа: '))
third_people = int(input('Введите возраст третьего соседа: '))

data = (first_people, second_people, third_people)
print(f'Сумма: {first_people + second_people + third_people}')
print(f'Среднее арифметическое: {sum(data) / len(data)} ')

