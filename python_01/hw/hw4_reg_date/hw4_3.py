import re 

def normalize_phone(phone_number):

    clear_phone_number = re.sub(r"[^+\d]", "", phone_number)
    print(clear_phone_number)

    pattern_dict = {r"\A\+38\d{3}\d{7}":"", 
                    r"\A38\d{3}\d{7}" : "+", 
                    r"\A\d{3}\d{7}" : "+38", 
                    r"\A\d{2}\d{7}":"+380"}

    for pattern, prefix in pattern_dict.items():
        if re.search(pattern, clear_phone_number):
            return f"{prefix}{clear_phone_number}"

    return "Invalid number"
  

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "38050+111+22+11"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

