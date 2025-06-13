

def input_error(func):
    def inner(args, contacts):
        try:
            return func(args, contacts)
        except ValueError as err:
            print(f"Error: Give me name and/or phone please\n{show_help()}")
        except KeyError as err:
            print(f"Error: This name is not added to contacts\n{show_help()}")
        except IndexError as err:
            print(f"IndexError: {err}")
    
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact {name} already exist"
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"Contact {name} doesn't exist"


@input_error
def show_phone(args, contacts):
    [name] = args
    return f"{name}:{contacts[name]}"


@input_error
def show_all_contacts(args, contacts):
    result = ""
    for name, phone in contacts.items():
        result+=f"{name}:{phone}\n"
    return result


@input_error
def say_hello(args, contacts):
    return "How can I help you?"


def show_help():
    return """Possible commands:
    hello - greeting
    add <username> <phone> - add new contact
    change <username> <phone> - modify existing contact
    phone <username> - print selected contact
    all - print all contacts
    close/exit - exit bot
    """

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    command_dct = {"hello":say_hello, 
                   "add": add_contact,
                   "change": change_contact,
                   "phone":show_phone,
                   "all":show_all_contacts}
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in command_dct.keys():
            print(command_dct[command](args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
