from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        return today_date.toordinal() - input_date.toordinal()
    except ValueError:
        print(f"Error! Cannot parse string {date} to datetime format." 
                "Date format must be YYYY-mm-dd")

days_str = get_days_from_today("2021-10-09")
print(days_str)

days_str = get_days_from_today("2021.10.09")
print(days_str)