# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

list_numbers = [random.randint(1, 20) for _ in range(20)]
start = int(input('Введите начальное число диапозона: '))
end = int(input('Введите конечное число диапозона: '))
list_index = []

for i in range(len(list_numbers)):
    if start < list_numbers[i] < end:
        list_index.append(i)

print(list_numbers)
print(f'Индексы чисел внутри диапозона: {list_index}')
