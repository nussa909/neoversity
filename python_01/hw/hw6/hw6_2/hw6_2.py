

def get_cats_info(path):
    result = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for el in file.readlines():
                try:
                    id, name, age = el.strip().split(",")
                    result.append({"id": id, "name":name, "age": age})
                except ValueError as err:
                    print(f"Error: {err}")
        
    except FileNotFoundError:
        print("Error: cannot open file!")
        
    return result



cats_info = get_cats_info( "cats_file.txt")
print(cats_info)