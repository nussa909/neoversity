import random

def get_numbers_ticket(min, max, quantity):
    if (min < 1 or max > 1000 or max - min < quantity):
        print(f"Error: Input parameters are not correct")
        return None
    
    try:
        random_list = random.sample(range(min,max), quantity)
        random_list.sort()
        return random_list
    except ValueError:
        print(f"Cannot generate values")
        return None
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("1,49,6:", lottery_numbers)

lottery_numbers = get_numbers_ticket(0, 49, 6)
print("0,49,6:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 1010, 6)
print("1,1010,6:", lottery_numbers)

lottery_numbers = get_numbers_ticket(100, 20, 6)
print("100,20,6:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 3, 6)
print("1,3,6:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 7, 6)
print("1,7,6:", lottery_numbers)