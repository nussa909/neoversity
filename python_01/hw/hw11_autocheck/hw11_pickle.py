import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fb:
        pickle.dump(contacts, fb)


def read_contacts_from_file(filename):
    with open(filename, "rb") as fb:
        return pickle.load(fb) 


some_data = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False
}]

file_name = "data.bin"

write_contacts_to_file(file_name, some_data)
print(read_contacts_from_file(file_name))