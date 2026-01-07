class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student {self.name} ({self.age} years old), ID: {self.student_id}"


p1 = Student("Tomm", 33, "STUDENT_ID")
print(p1)
