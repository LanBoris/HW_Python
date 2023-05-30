import text
import view
import model

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_phone_book()
                view.print_message(text.success_loading)
            case 2:
                model.save_phone_book()
                view.print_message(text.success_saving)
            case 3:
                book = model.show_phone_book()
                view.print_contacts(book, text.empty_phone_book)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_success_loading(name))
            case 5:
                word = view.input_search(text.input_search)
                result = model.search_contact(word)
                view.print_contacts(result, text.empty_search(word))
            case 6:
                word = view.input_search(text.input_change_contact)
                result = model.search_contact(word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index_of_contact)
                    else:
                        current_id = result[0].get('id')
                    new_contact = view.input_contact(text.change_contact)
                    name = model.change_contact(new_contact, current_id)
                    view.print_message(text.success_changing(name))
                else:
                    view.print_message(text.empty_search(word))
            case 7:
                word = view.input_search(text.input_delete_contact)
                result = model.search_contact(word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_index(text.input_index_of_contact)
                    else:
                        current_id = result[0].get('id')
                    del_contact = view.delete_contact(text.deleting_contact)
                    name = model.delete_contact(del_contact, current_id)
                    view.print_message(text.delete_contact(name))
                else:
                    view.print_message(text.empty_search(word))
            case 8:
                break