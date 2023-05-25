# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
# “Пам парам”, если с ритмом все не в порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

def analysis_text(input_text):
    text_analysis = input_text.split()
    list_counts = list()
    for i in text_analysis:
      count_letters = sum(map(lambda x: x in 'ёуеыаоэяию', i))
      list_counts.append(count_letters)
    first_sum = list_counts[0]
    list_counts = set(map(lambda x: x == first_sum, list_counts))
    if len(list_counts) == 1:
       print('Парам пам-пам')
    else: 
       print('Пам парам')
      
print('Как вводим текст?\n' 
      + '1. Берем готовый текст.\n' 
      + '2. Введем с клавиатуры.\n')
answer = int(input('Введите номер ответа: '))
if answer == 1:
  vinni_text = 'пара-ра-рам рам-пам-папам па-ра-па-да'
  print(vinni_text)
elif answer == 2:
  vinni_text = input('Введите текст: ')
else: print('Нет такого варианта ответа.')

analysis_text(vinni_text)