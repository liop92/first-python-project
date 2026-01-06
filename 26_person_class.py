class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello my name is {self.name}, and i am {self.age} years old!")


p1 = Person("Tomm", 33)

p1.say_hello()
