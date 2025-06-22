class IDException(Exception):
    pass


def add_id(id_list, employee_id : str):
    if employee_id[0:2] == "01":
        id_list.append(employee_id)
    else:
        raise IDException("Wrong id")
    return id_list


list = ["01_Anna", "01_Ivan"]

eid_1 = "01_John"
eid_2 = "David"

try:
    print(add_id(list,eid_1))
    print(add_id(list,eid_2))
except IDException as ex:
    print(ex)
