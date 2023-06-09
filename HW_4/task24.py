# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# Example:
# 4 -> 1 2 3 4
# 9

import random

number_of_bushes = int(input('Введите кол-во кустов: '))
amount_berries = []
max_summ_berries = 0

for i in range(number_of_bushes):
    amount_berries.append(random.randint(1,10))

for i in range(len(amount_berries)):
    sum_berries = amount_berries[i-2] + amount_berries[i-1] + amount_berries[i]
    if sum_berries > max_summ_berries: max_summ_berries = sum_berries

print(f'Список с количеством ягод на каждом кусте: {amount_berries}')
print(f'Максимальное число ягод, за один заход: {max_summ_berries}')