class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Meow"
    
    def change_weight(self, weight):
        self.weight = weight
    
class Recorder:
    def record_animal(self, animal):
        voice = animal.say()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat("Simon", 10)
strange_animal = CatDog("CatDog", 50)

r.record_animal(cat)  # Recorded "Meow!"
r.record_animal(strange_animal)  # Recorded "Meow"