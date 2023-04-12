'''
Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
'''
import random

summ = int(input('Введите сумму чисел: '))
multiply = int(input('Введите произведение чисел: '))
number_1 = 0
number_2 = 0
flag = False
while (flag == False):
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)
    if number_1 + number_2 == summ and number_1 * number_2 == multiply: flag = True
    else: flag = False
print(f'Петя загадал: {number_1,number_2}')
