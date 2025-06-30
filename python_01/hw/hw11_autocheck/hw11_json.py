import json


def write_contacts_to_file(filename, contacts):
    contact_dict = {"contacts": contacts}
    with open(filename, "w") as file:
        json.dump(contact_dict, file)
        


def read_contacts_from_file(filename):
    with open(filename, "r") as file:
        return json.load(file)["contacts"]


some_data = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False
}]


file_name = "data.json"


write_contacts_to_file(file_name, some_data)
print(read_contacts_from_file(file_name))