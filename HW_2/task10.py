'''
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
'''
import random

amount_coins = int(input('Введите кол-во монеток на столе: '))
coin = 0
list_coins = []
count_zero = 0
count_ones = 0

for i in range(1,amount_coins+1):
    coin = random.randint(0,1)
    list_coins.append(coin)
    if coin == 0: count_zero += 1
    else: count_ones += 1

print(list_coins)
if count_ones > count_zero:
   print(f'Нужно перевернуть {count_zero}.')
else:
   print(f'Нужно перевернуть {count_ones}.')


