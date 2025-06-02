def format_string(string, length):
    if len(string) >= length: 
        return string
    else:
        spaces_num = (length - len(string)) // 2
        return " " * spaces_num + string


print(format_string("Hello", 20))