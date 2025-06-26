from collections import UserDict
import re 


class ValidationError(Exception):
    pass


class PhoneNotFoundError(Exception):
    pass


class InputError(Exception):
    pass


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as err:
            print(f"ValidationError: {err}")
        except PhoneNotFoundError as err:
            print(f"PhoneNotFoundError: {err}")
        except InputError as err:
            print(f"InputError: {err}")
        except KeyError as err:
            print(f"KeyError: {err}")
        except ValueError as err:
            print(f"ValueError: {err}")
    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass
       

class Phone(Field):
    def __init__(self, value):
        self.__validate_item(value)
        super().__init__(value)
        
    def __validate_item(self, phone : str):
        match = re.match(r"^\d{10}$", phone)
        if match == None:
            message = f"validation of phone number {phone} failed"
            raise ValidationError(message) 


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @error_handler
    def add_phone(self, phone:str):
        if self.__is_phone_added(phone):
            raise InputError(f"phone {phone} has already added")
        else: 
            self.phones.append(Phone(phone))
    
    @error_handler
    def edit_phone(self, old_phone:str, new_phone:str):
        if old_phone == new_phone:
            raise InputError("new phone should differ from previous one")
        
        index = self.__find_idx_by_phone(old_phone)
        if index != None:
            self.phones[index] = Phone(new_phone)

    @error_handler   
    def remove_phone(self, phone:str):
        self.phones.remove(self.find_phone(phone))
    
    @error_handler
    def find_phone(self, phone:str):
        index = self.__find_idx_by_phone(phone)
        if index != None:
            return self.phones[index]

    def __is_phone_added(self, phone):
        for phone_item in self.phones:
            if phone_item.value == phone:
                return True
            
        return False

    def __find_idx_by_phone(self, phone:str)->int:
        for index, phone_item in enumerate(self.phones):
            if phone_item.value == phone:
                return index

        raise PhoneNotFoundError(f"phone {phone} was not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    @error_handler
    def add_record(self, record:Record):
        self.data.update({ record.name.value : record })

    @error_handler
    def find(self, name:str):
        return self.data.get(name)

    @error_handler
    def delete(self, name:str):
        self.data.pop(name)
    
    def __str__(self):
        str = "Address book:"
        for name, record in self.data.items():
            str += f"{name}:{record}; "

        return str


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

nussa_record = Record("Nussa")
nussa_record.add_phone("9999999999")
nussa_record.add_phone("8888888888")
book.add_record(nussa_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)
print("*" * 40)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
john.remove_phone(found_phone.value)

# Видалення запису Jane
book.delete("Jane")

print("*" * 40)
for name, record in book.data.items():
    print(record)