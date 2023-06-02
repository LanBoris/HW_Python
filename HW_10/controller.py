import text
import view
import model
import numbers

my_table = model.TablePlayers()

def start():
    my_table.open_table_players()
    view.print_message(text.hello_message)
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                table_players = my_table.show_table_players()
                view.print_table_players(table_players, text.empty_table_players)
            case 2:
                player = view.input_player(text.input_new_player)
                name = my_table.add_player(player)
                view.print_message(text.new_player_success_loading(name))
            case 3:
                amount = int(view.input_amount_ex(text.amount_exercise))
                count = 0
                for i in range(0, amount):
                    num_one, num_two = numbers.number(), numbers.number()
                    result = numbers.sum_num(num_one, num_two)
                    player_result = view.input_result(text.sum_input(num_one, num_two))
                    if result == player_result: 
                        view.print_check_answer(text.right_answer)
                        count += 1
                    else: 
                        view.print_check_answer(text.wrong_answer)
                        count -= 1
                player = view.input_name(text.search_player)
                my_table.count_points(player, count)
                view.print_message(text.add_result(player))
            case 4:
                amount = int(view.input_amount_ex(text.amount_exercise))
                count = 0
                for i in range(0, amount):
                    num_one, num_two = numbers.number(), numbers.number()
                    result = numbers.diff_num(num_one, num_two)
                    player_result = view.input_result(text.diff_input(num_one, num_two))
                    if result == player_result: 
                        view.print_check_answer(text.right_answer)
                        count += 1
                    else: 
                        view.print_check_answer(text.wrong_answer)
                        count -= 1
                player = view.input_name(text.search_player)
                my_table.count_points(player, count)
                view.print_message(text.add_result(player))
            case 5:
                amount = int(view.input_amount_ex(text.amount_exercise))
                count = 0
                for i in range(0, amount):
                    num_one, num_two = numbers.number_multi(), numbers.number_multi()
                    result = numbers.multi_num(num_one, num_two)
                    player_result = view.input_result(text.multi_input(num_one, num_two))
                    if result == player_result: 
                        view.print_check_answer(text.right_answer)
                        count += 3
                    else: 
                        view.print_check_answer(text.wrong_answer)
                        count -= 3
                player = view.input_name(text.search_player)
                my_table.count_points(player, count)
                view.print_message(text.add_result(player))
            case 6:
                amount = int(view.input_amount_ex(text.amount_exercise))
                count = 0
                for i in range(0, amount):
                    num_one, num_two = numbers.number_multi(), numbers.number_multi()
                    if num_one > num_two:
                        result = numbers.division_num(num_one, num_two)
                        player_result = view.input_result(text.division_input(num_one, num_two))
                        if result == player_result: 
                            view.print_check_answer(text.right_answer)
                            count += 3
                        else: 
                            view.print_check_answer(text.wrong_answer)
                            count -= 3
                    else:
                        result = numbers.division_num(num_two, num_one)
                        player_result = view.input_result(text.division_input(num_two, num_one))
                        if result == player_result: 
                            view.print_check_answer(text.right_answer)
                            count += 3
                        else: 
                            view.print_check_answer(text.wrong_answer)
                            count -= 3
                player = view.input_name(text.search_player)
                my_table.count_points(player, count)
                view.print_message(text.add_result(player))
            case 7:
                my_table.save_table_players()
                view.print_message(text.saving_result(player.upper()))
            case 8:
                break