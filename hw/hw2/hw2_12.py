def first(size, *args):
    return size + len(args)

def second(size, **kwargs):
    return size + len(kwargs)


print(first(5,"first","second","third"))    # Результат: 8
print(first(1, "Alex", "Boris"))            # Результат: 3
print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12