class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


dev = Developer("Ana", 5000, "Python")
print(dev.name, dev.salary, dev.programming_language)
