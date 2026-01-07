class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Animal sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


animals = [Dog("Buddy"), Cat("Garfield")]

for animal in animals:
    print(animal.speak())
