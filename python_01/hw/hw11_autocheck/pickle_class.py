import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
       self.name = name
       self.email = email
       self.phone = phone
       self.favorite = favorite 

    def __repr__(self):
        return f"name:{self.name},email:{self.email},phone:{self.phone},favorite:{self.favorite}"

    def __str__(self):
        return f"Person{{ name:{self.name},email:{self.email},phone:{self.phone},favorite:{self.favorite} }}"
 

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        
        self.filename = filename
        self.contacts = contacts
        
  
    def save_to_file(self):
        with open(self.filename, "wb") as fb:
            pickle.dump(self, fb)
            

    def read_from_file(self):
        with open(self.filename, "rb") as fb:
            return pickle.load(fb) 

    def __str__(self):
        return f"filename:{self.filename}, contacts{[contact for contact in self.contacts]}"

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()

print(persons)
print(person_from_file)

print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True