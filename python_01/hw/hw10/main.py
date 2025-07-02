from addressbook import AddressBook, Record, error_handler, InputError


def unpack_args(args, max_args):
    return (args + [None] * max_args)[:max_args]


@error_handler
def add_contact(args, book: AddressBook):
    name, phone, birthday = unpack_args(args, 3)

    if not name or not phone:
        raise InputError("add_contact: name or phone of contact was not entered")
    
    record = book.find(name)
    message = f"Contact {name} updated"

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added"

    if phone:
        record.add_phone(phone)

    if birthday:
        record.add_birthday(birthday)

    return message


@error_handler
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, birthday = unpack_args(args, 4)

    if not name or not old_phone or not new_phone:
        raise InputError("change_contact: name, old or new phone of contact was not entered")
    
    record = book.find(name)
    message = f"Contact {name} updated"

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added"

    if old_phone and new_phone:
        record.edit_phone(old_phone, new_phone)

    if birthday:
        record.add_birthday(birthday)
    return message


@error_handler
def show_phone(args, book: AddressBook):
    [name] = unpack_args(args, 1)

    if not name:
        raise InputError("show_phone: name of contact was not entered")

    record = book.find(name)
    if record:
        return f"{', '.join(p.value for p in record.phones)}"


@error_handler
def show_all_contacts(args, book):
    result = f"{book}"
    return result


@error_handler
def say_hello(args, book: AddressBook):
    return "How can I help you?"


@error_handler
def add_birthday(args, book):
    name, birthday = unpack_args(args, 2)

    if not name or not birthday:
        raise InputError(
            "add_birthday: name or birthday of contact was not entered")

    record = book.find(name)
    message = f"Contact {name} updated"

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added"

    record.add_birthday(birthday)

    return message


@error_handler
def show_birthday(args, book: AddressBook):
    [name] = unpack_args(args, 1)

    if not name:
        raise InputError("show_birthday: name of contact was not entered")
    
    record = book.find(name)
    if record:
        return f"{record.birthday}"


@error_handler
def birthdays(args, book: AddressBook):
    return book.get_upcoming_birthdays()


@error_handler
def show_help():
    return """Possible commands:
    hello - greeting
    help - show help message
    add <username> <phone> <birthday> - add new contact
    change <username> <old phone> <new phone> <birthday> - modify existing contact
    phone <username> - print phone for dedicated contact
    all - print all contacts
    add-birthday <name> <birthday> - add birthday to contact
    show-birthday <name> - show birthday for dedicated contact
    birthdays - show contact who will celebrate birthday in next 7 days
    close/exit - exit bot
    """


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    command_dct = {"hello": say_hello,
                   "help":show_help,
                   "add": add_contact,
                   "change": change_contact,
                   "phone": show_phone,
                   "all": show_all_contacts,
                   "add-birthday": add_birthday,
                   "show-birthday": show_birthday,
                   "birthdays": birthdays}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in command_dct.keys():
            print(command_dct[command](args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()


# book = AddressBook()
# print(add_contact(["Nussa", "0123456789", "17.04.1989"], book))
# print(add_contact(["John wick", "1111111111"], book))
# print(add_contact(["Victor"], book))
# print(add_contact([],book))
# print(show_all_contacts([],book))
# print(add_contact(["Victor", "5555555555"], book))
# print(show_all_contacts([],book))
# print(add_contact(["Victor", "5555555555","11.01.2000"], book))
# print(show_all_contacts([],book))
# print(change_contact(["Victor","5555555555", "7777777777"], book))
# print(show_all_contacts([],book))
# print(change_contact(["Alina","", "8888888888"], book))
# print(change_contact(["Alina","8888888888"], book))
# print(show_all_contacts([],book))
# print(show_phone(["Nussa"], book))
# print(show_phone(["Nuke"], book))
# print(add_birthday(["Alina" ],book))
# print(add_birthday(["Alina", "15.02.1989"],book))
# print(show_birthday(["Alina"],book))
# print(add_birthday(["Alina", "07.07.1989"],book))
# print(birthdays([],book))
# print(add_contact(["Nuke", "1234"],book))
# print(add_contact(["Luke", "9999999999", "20-12-2010"],book))


