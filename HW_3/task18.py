# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

list_numbers = []
size_of_list = int(input('Введите размер списка: '))
number = int(input('Введите число Х: '))

for i in range(size_of_list):
    list_numbers.append(random.randint(1, size_of_list))

find_num = list_numbers[0]

for i in range(size_of_list):
    if abs(list_numbers[i] - number) < abs(find_num - number):
        find_num = list_numbers[i]

print(f'Список для проверки:\n{list_numbers}')
print(f'Самое близкое число: {find_num}')
