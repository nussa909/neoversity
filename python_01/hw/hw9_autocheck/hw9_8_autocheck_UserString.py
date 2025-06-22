from collections import UserString


class NumberString(UserString):
    def number_count(self):
        sum = 0
        for char in self.data:
            if char.isdigit():
                sum += 1
        return sum

str = NumberString("hello 1 worlds 3456")
print(str.number_count())
