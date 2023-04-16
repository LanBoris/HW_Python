# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12

one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_points = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
three_points = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
four_points = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
five_points = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
eight_points = ['J', 'X', 'Ш', 'Э', 'Ю']
ten_points = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

counter = 0
word = input('Введите слово: ')

for i in range(len(word)):
    symbol = word[i].upper()
    if symbol in one_point:
        counter += 1
    elif symbol in two_points:
        counter += 2
    elif symbol in three_points:
        counter += 3
    elif symbol in four_points:
        counter += 4
    elif symbol in five_points:
        counter += 5
    elif symbol in eight_points:
        counter += 8
    elif symbol in ten_points:
        counter += 10
    else: counter += 0
print(f'Ваше слово стоит: {counter}')