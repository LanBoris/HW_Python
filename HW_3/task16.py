# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в списке A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в списке. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

list_numbers = []
size_of_list = int(input('Введите количество элементов списка: '))
number = int(input(f'Введите искомое число в интревале от 1 до {size_of_list}: '))
counter = 0

for i in range(size_of_list):
    list_numbers.append(random.randint(1, size_of_list))
    if list_numbers[i] == number:
        counter += 1

print(f'Список для прокерки:\n{list_numbers}')
print(f'Искомое число {number} встречается в списке {counter} раз.')