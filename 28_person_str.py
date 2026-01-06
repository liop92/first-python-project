class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello my name is {self.name}, and i am {self.age} years old!"


p1 = Person("Tomm", 33)
p2 = Person("Mike", 42)
p3 = Person("Susan", 28)

print(p1)
print(p2)
print(p3)
