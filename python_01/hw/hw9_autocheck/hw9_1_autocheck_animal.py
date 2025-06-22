class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.__nickname = nickname
        self.__weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.__weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal("Simon", 10)
second_animal = Animal("Sharik", 12)

first_animal.change_color("red")

print(first_animal.color)
print(second_animal.color)