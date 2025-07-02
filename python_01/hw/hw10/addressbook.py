from collections import UserDict
import re
from datetime import datetime


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
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.__validate_item(value)
        super().__init__(value.title())

    def __validate_item(self, name: str):
        if type(str) != type(str):
            message = f"Validation of name {name} failed. str type expected"
            raise ValidationError(message)


class Phone(Field):
    def __init__(self, value):
        self.__validate_item(value)
        super().__init__(value)

    def __validate_item(self, phone: str):
        match = re.match(r"^\d{10}$", phone)
        if match == None:
            message = f"Validation of phone number {phone} failed. 10 digits expected"
            raise ValidationError(message)


class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, "%d.%m.%Y"))
        except ValueError:
            raise ValidationError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return str(datetime.strftime(self.value, "%d.%m.%Y"))

    def __repr__(self):
        return str(datetime.strftime(self.value, "%d.%m.%Y"))


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        if not self.__is_phone_added(phone):
            self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        if old_phone == new_phone:
            raise InputError("new phone should differ from previous one")

        index = self.__find_idx_by_phone(old_phone)
        if index != None:
            self.phones[index] = Phone(new_phone)

    def remove_phone(self, phone: str):
        self.phones.remove(self.find_phone(phone))

    def find_phone(self, phone: str):
        index = self.__find_idx_by_phone(phone)
        if index != None:
            return self.phones[index]

    def __is_phone_added(self, phone):
        for phone_item in self.phones:
            if phone_item.value == phone:
                return True

        return False

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def __find_idx_by_phone(self, phone: str) -> int:
        for index, phone_item in enumerate(self.phones):
            if phone_item.value == phone:
                return index

        raise PhoneNotFoundError(f"phone {phone} was not found")

    def __str__(self):
        return f"name:{self.name.value}, phones: {', '.join(p.value for p in self.phones)}, birthday:{self.birthday}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data.update({record.name.value.lower(): record})

    def find(self, name: str):
        return self.data.get(name.lower())

    def delete(self, name: str):
        self.data.pop(name.lower())

    def get_upcoming_birthdays(self):
        condratulation_dct = {}
        records = filter(lambda rec: rec.birthday != None, self.data.values())

        for record in records:
            today_date = datetime.today()

            birthday_this_year = record.birthday.value.replace(
                year=today_date.year)
            
            birthday_next_year = record.birthday.value.replace(
                year=today_date.year+1)
            
            next_birthday = birthday_this_year if birthday_this_year > today_date else birthday_next_year

            days_to_birthday = next_birthday.toordinal() - today_date.toordinal()
            
            if days_to_birthday <= 7:
                condratulation_day = next_birthday.replace(
                    day=next_birthday.day + 7 - next_birthday.weekday()) if next_birthday.weekday() >= 5 else next_birthday
                condratulation_dct.update(
                    {record.name: datetime.strftime(condratulation_day, "%d.%m.%Y")})

        return condratulation_dct

    def __str__(self):
        str = "Address book:\n"
        for name, record in self.data.items():
            str += f"{record}\n"

        return str


# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# nussa_record = Record("Nussa")
# nussa_record.add_phone("9999999999")
# nussa_record.add_phone("8888888888")
# book.add_record(nussa_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)
# print("*" * 40)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
# john.remove_phone(found_phone.value)

# # Видалення запису Jane
# book.delete("Jane")

# print("*" * 40)
# for name, record in book.data.items():
#    print(record)

# book = AddressBook()
# record_nussa = Record("Nussa")
# record_nussa.add_phone("0123456789")
# record_nussa.add_birthday("17.04.1989")
# book.add_record(record_nussa)
# record_john = Record("John")
# record_john.add_phone("9876543210")
# record_john.add_birthday("01.07.1990")
# book.add_record(record_john)

# print(book.get_upcoming_birthdays())
