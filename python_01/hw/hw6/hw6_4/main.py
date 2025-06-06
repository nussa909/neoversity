
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact {name} already exist"
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"Contact {name} doesn't exist"

def show_phone(args, contacts):
    [name] = args
    return f"{name}:{contacts[name]}"

def show_all_contacts(args, contacts):
    result = ""
    for name, phone in contacts.items():
        result+=f"{name}:{phone}\n"
    return result

def say_hello(args, contacts):
    return "How can I help you?"

def show_help():
    return """Possible commands:
    hello - greeting
    add <username> <phone> - add new contact
    change <username> <phone> - modify existing contact
    phone <username> - print selected contact
    all - print all contact
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
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command in command_dct.keys():
                print(command_dct[command](args, contacts))
            else:
                print("Invalid command.")
        except Exception as err:
            print(f"Error: {err}\n {show_help()}")


if __name__ == "__main__":
    main()
