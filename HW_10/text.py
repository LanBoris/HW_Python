hello_message = '''Привет!!!\nДавай порешаем примеры по математике!!!'''

main_menu = '''\nГлавное меню:
1. Посмотреть таблицу игроков.
2. Создать нового игрока.
3. Примеры на сложение (1 балл).
4. Примеры на вычитание (1 балла).
5. Примеры на умножение (3 балла).
6. Примеры на целочисленное деление (3 балла).
7. Записать свой результат в таблицу.
8. Выход
_________________________________
Правильный ответ - плюс баллы,
Неправильный ответ - минус баллы.\n'''

input_choice = '''Введите номер пункта меню: '''

empty_table_players = 'Таблица игроков пуста.'

input_new_player = 'Новый игрок:'

new_player = {'name': 'Введите имя: '}
search_player = 'Введите имя: '

def new_player_success_loading(name: str) -> str:
    return f'Игрок {name} успешно создан.'

def add_result(name: str) -> str:
    return f'Результат игрока {name} внесен в таблицу.'

def saving_result(name: str) -> str:
    return f'Результат игрока {name} сохранен в таблице.'

amount_exercise = 'Сколько примеров хотите решить: '

def sum_input(num_one: int, num_two: int) -> int:
    result = f'{num_one} + {num_two} = ' 
    return result

def multi_input(num_one: int, num_two: int) -> int:
    result = f'{num_one} * {num_two} = ' 
    return result

def diff_input(num_one: int, num_two: int) -> int:
    result = f'{num_one} - {num_two} = ' 
    return result

def division_input(num_one: int, num_two: int) -> int:
    result = f'{num_one} : {num_two} = ' 
    return result

right_answer = '~ВЕРНО~'
wrong_answer = '~ОШИБКА~'