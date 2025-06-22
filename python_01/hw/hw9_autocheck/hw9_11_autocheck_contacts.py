
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({  "id": Contacts.current_id,
                                "name": name,
                                "phone": phone,
                                "email": email,
                                "favorite": favorite })
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
    
    def remove_contacts(self, id):
        self.contacts.remove(self.get_contact_by_id(id))


contacts = Contacts()
contacts.add_contacts("John", "123456789","john@gmail.com", False)
contacts.add_contacts("David", "987654321","david@gmail.com", True)
print(contacts.contacts)
print(contacts.get_contact_by_id(1))
contacts.remove_contacts(2)
print(contacts.contacts)