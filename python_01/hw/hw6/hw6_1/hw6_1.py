def total_salary_file(file):
    total = 0
    lines = file.readlines()
    for el in lines:
        try:
            _, salary = el.strip().split(",")
            total += int(salary)
        except ValueError as err:
            print(f"Error: {err}")

    return (total, total // len(lines))


def total_salary(path):
    try:
        with open(path, "r",encoding="utf-8") as file:
            return total_salary_file(file)
   
    except FileNotFoundError:
        print("Error: cannot open file!")
    
    return (0,0)
        

total, average = total_salary( "salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")