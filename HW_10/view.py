import text
import numbers

def main_menu() -> int:
    print(text.main_menu)
    while True:
      choice = input(text.input_choice)
      if choice.isdigit() and 0 < int(choice) < 9:
          return int(choice)
      
def print_message(message):
   print('\n' + '~'*len(message))
   print(message)
   print('~'*len(message) + '\n')

def print_table_players(tab_players: list[dict[str, str]], error: str):
   if tab_players:
      print('\n' + '~'*80)
      for player in tab_players:
         print(f'{player.get("id"):>3}. {player.get("name"):<10} - {player.get("score"):^10}')
      print('~'*80 + '\n')
   else:
      print_message(error)

def input_player(message) -> dict[str, str]:
   new = {}
   print(message)
   for key, txt in text.new_player.items():
      value = input(txt)
      if value:
         new[key] = value
   return new

def input_amount_ex(message) -> int:
   return input(message)
   
def input_result(message) -> int:
   return int(input(message))

def print_check_answer(message):
   print(message)

def input_name(message) -> str:
   name = input(message)
   return name