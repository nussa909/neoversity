import csv

def str_to_bool(value: str):
    # match value:
    #     case "True": return True
    #     case "False": return False
    #     case _: None
    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        return None


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        field_names = contacts[0].keys()
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

    
    
def read_contacts_from_file(filename):
    with open(filename, "r", newline='') as fh:
        reader = csv.DictReader(fh)
        result = []
        for row in reader:
            row.update({"favorite" : str_to_bool(row["favorite"])})
            result.append(row)
    return result


some_data = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False
}]

file_name = "data.csv"

write_contacts_to_file(file_name, some_data)
print(read_contacts_from_file(file_name))
