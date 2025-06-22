class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def info(self):
        return f"{self.nickname} - {self.weight}"


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"
    

class CatDog(Cat,Dog):
    pass
    

class DogCat(Dog,Cat):
    pass


cat = Cat("Simon", 5)
dog = Dog("Sharik", 10)
cat_dog = CatDog("CatDog", 23)
dog_cat = DogCat("DogCat", 40)

print(cat.info())
print(dog.info())
print(cat_dog.info())
print(dog_cat.info())