# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Example:
# 2 2
# 4

def sum_rec(number_1: int, number_2: int):
    if number_1 == 0:
        return number_2
    if number_2 == 0:
        return number_1
    else: 
        return sum_rec(number_1 - 1, number_2 + 1)

number_a = int(input('Введите число A: '))
number_b = int(input('Введите число B: '))

if number_a >= 0 and number_b >= 0:
    print(f'Сумма чисел А={number_a} и B={number_b} равна: {sum_rec(number_a, number_b)}')
else: print('Вы ввели отрицательное цисло.')