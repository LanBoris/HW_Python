'''
Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
'''

number = int(input('Введите число: '))
degree = 0
list = []
while 2**degree < number:
    list.append(2**degree)
    degree += 1
print(list)