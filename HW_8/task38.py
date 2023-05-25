# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def show_all_contacts(input_list):
  for line in input_list:
    print(line)

def add_contact(input_list):
  print('Enter new contact')
  new_name = input('Enter name: ')
  new_phone = input('Enter phone: ')
  new_comment = input('Enter comment: ')
  input_list.append(new_name + ' ' + new_phone + ' ' + new_comment)
  return input_list

def find_contact(input_list):
  find_metric = input('Enter metric to find: ')
  print('Found contacts:')
  for i in input_list:
    if find_metric in i:
      print(i)
  print()

def change_contact(input_list):
  list_enumerate = list(enumerate(input_list, 1))
  for i in list_enumerate: 
    print(*i)
  id_contact = int (input('Enter id of contact to change: ')) - 1
  input_list[id_contact] = input('Enter new name, phone, comment: ')
  return input_list

def delete_contact(input_list):
  list_enumerate = list(enumerate(input_list, 1))
  for i in list_enumerate:
    print(*i)
  id_contact = int (input('Enter id of contact to delete: ')) - 1
  del input_list[id_contact]
  return input_list

def print_menu():
  print('\n' + 'Work with phone book menu:\n'
        +'1. Show all contacts.\n'
        +'2. Add new contact.\n'
        +'3. Find contact.\n'
        +'4. Change contact.\n'
        +'5. Delete contact.\n'
        +'6. Exit.\n')

path = 'phone_book.txt'
file_base = open(path, 'r')
data = file_base.read()
file_base.close()
data = data.split('\n')
data = list(filter(None, data))

print_menu()
choice = int(input('Enter number of your choice: '))
while choice != 6:
  if choice == 1: 
    show_all_contacts(data)
    print_menu()
    choice = int(input('Enter number of your choice: '))
  elif choice == 2: 
    add_contact(data)
    print_menu()
    choice = int(input('Enter number of your choice: '))
  elif choice == 3: 
    find_contact(data)
    print_menu()
    choice = int(input('Enter number of your choice: '))
  elif choice == 4: 
    change_contact(data)
    print_menu()
    choice = int(input('Enter number of your choice: '))
  elif choice == 5: 
    delete_contact(data)
    print_menu()
    choice = int(input('Enter number of your choice: '))
  elif choice == 6: exit()
  else: 
    print('Wrong choice.')
    print_menu()
    choice = int(input('Enter number of your choice: '))

file_base = open(path, 'w')
data = list(map(lambda x: x + '\n', data))
data = list(filter(None, data))
file_base.writelines(data)
file_base.close()