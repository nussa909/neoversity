from addressbook import AddressBook, Record
from file_serializer import FileSerializer
from exceptions import error_handler, InputError


def unpack_args(args, max_args):
    return (args + [None] * max_args)[:max_args]


############################ bot's commands #########################################
@error_handler
def add_contact(args, book):
    name, phone, birthday = unpack_args(args, 3)

    if not name or not phone:
        raise InputError(
            "add_contact: name or phone of contact was not entered")

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
def change_contact(args, book):
    name, old_phone, new_phone, birthday = unpack_args(args, 4)

    if not name or not old_phone or not new_phone:
        raise InputError(
            "change_contact: name, old or new phone of contact was not entered")

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
def show_phone(args, book):
    [name] = unpack_args(args, 1)

    if not name:
        raise InputError(
            "show_phone: name of contact was not entered")

    record = book.find(name)
    if record:
        return f"{', '.join(p.value for p in record.phones)}"


@error_handler
def show_all_contacts(args, book):
    return f"{book}"


@error_handler
def say_hello(args, _):
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
def show_birthday(args, book):
    [name] = unpack_args(args, 1)

    if not name:
        raise InputError(
            "show_birthday: name of contact was not entered")

    record = book.find(name)
    if record:
        return f"{record.birthday}"


@error_handler
def birthdays(args, book):
    print("People to congratulate next week:")
    return '\n'.join(f"{name} : {birthday}" for name, birthday in book.get_upcoming_birthdays().items())


@error_handler
def show_help(args, _):
    message = """Possible commands:
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
    return message


@error_handler
def say_bye(args, bot):
    bot.stop()
    return "Good bye!"
##############################################################################


class Command:
    def __init__(self, command, func, receiver):
        self.command = command
        self.func = func
        self.receiver = receiver

    def __eq__(self, command):
        return self.command == command

    def __call__(self, args):
        return self.func(args, self.receiver)


class ConsoleBot:

    def __init__(self):
        self.__serializer = FileSerializer("addressbook.pkl")
        self.__book = AddressBook()
        self.load_data()
        self.__commands = [Command("hello", say_hello, self.__book),
                           Command("help", show_help, self.__book),
                           Command("add", add_contact, self.__book),
                           Command("change", change_contact, self.__book),
                           Command("phone", show_phone, self.__book),
                           Command("all", show_all_contacts, self.__book),
                           Command("add-birthday", add_birthday, self.__book),
                           Command("show-birthday",
                                   show_birthday, self.__book),
                           Command("birthdays", birthdays, self.__book),
                           Command("close", say_bye, self),
                           Command("exit", say_bye, self)]
        self.__is_running = False

    def save_data(self):
        self.__serializer.save_data(self.__book)

    def load_data(self):
        loaded_data = self.__serializer.load_data()
        if loaded_data != None:
            self.__book = loaded_data

    def start(self):
        print("Welcome to the assistant bot!")
        self.__is_running = True
        while self.__is_running:
            user_input = input("Enter a command: ")
            command, *args = self.__parse_input(user_input)

            try:
                index = self.__commands.index(command)
                print(self.__commands[index](args))
            except ValueError:
                print("Invalid command.")

        self.save_data()

    def stop(self):
        self.__is_running = False

    def __parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args


if __name__ == "__main__":
    console_bot = ConsoleBot()
    console_bot.start()
