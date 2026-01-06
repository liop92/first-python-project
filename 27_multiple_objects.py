class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello my name is {self.name}, and i am {self.age} years old!")


p1 = Person("Tomm", 33)
p2 = Person("Mike", 42)
p3 = Person("Susan", 28)

p1.say_hello()
p2.say_hello()
p3.say_hello()

print("---AND---")


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def enter(self):
        return f"Hello my name is {self.name}, and i am {self.age} years old!"


p1 = Person2("Tomm", 33)
p2 = Person2("Mike", 42)
p3 = Person2("Susan", 28)

print(p1.enter())
print(p2.enter())
print(p3.enter())
