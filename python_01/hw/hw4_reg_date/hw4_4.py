from datetime import datetime

def get_upcoming_birthdays(users):
    condratulation_dct = {}
    for user in users:
        try:
            birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            today_date = datetime.today().date()
            birthday_this_year = birthday_date.replace(year=today_date.year)   
            birthday_next_year = birthday_date.replace(year=today_date.year+1) 
            next_birthday = birthday_this_year if birthday_this_year > today_date else birthday_next_year

            days_to_birthday = next_birthday.toordinal() - today_date.toordinal()
            if days_to_birthday <= 7:
                condratulation_day = next_birthday.replace(day=next_birthday.day + 7 - next_birthday.weekday() ) if next_birthday.weekday() >= 5 else next_birthday 
                condratulation_dct.update({user["name"] : condratulation_day})
        except ValueError as err:
            print(f"Error:{err}")
            continue
    return condratulation_dct


users = [
    {"name": "John Doe", "birthday": "1985.06.01"},
    {"name": "Jane Smith", "birthday": "1990.06.03"},
    {"name": "Will Smith", "birthday": "19efekfekfe"},
    {"name": "Will Smith", "birthday": "1970.09.13"},
    {"name": "Will Smith", "birthday": "19efekfekfe"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

