main_menu = '''\nГлавное меню
1. Открыть файл
2. Сохранить Файл
3. Показать контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход\n'''

input_choice = '''Введите номер пункта меню: '''

success_loading = 'Телефонная книга успешно загружена.'

success_saving = 'Телефонная книга успешно сохранена.'

empty_phone_book = 'Телефонная книга пуста.'

input_new_contact = 'Введите новый контакт:'
new_contact = {'name': 'Введите имя: ', 
               'phone': 'Введите номер телефона: ', 
               'comment': 'Введите комментарий: '}

def new_contact_success_loading(name: str) -> str:
    return f'Контакт {name} успешно сохранен.'

input_search = 'Поиск: '

def empty_search(word) -> str:
    return f'Контакты содержащие "{word}" не найдены.'

input_change_contact = 'Какой контакт будем изменять: '

input_index_of_contact = 'Введите ID контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтобы не изменять.'

def success_changing(name: str) -> str:
    return f'Контакт {name} успешно изменен.'

input_delete_contact = 'Какой контакт хотите удалить: '

deleting_contact = 'Этот контакт будет удален.'

def delete_contact(name: str) -> str:
    return f'Контакт {name} успешно удален.'
