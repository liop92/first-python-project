try:
    a = input("Give me a number: ")
    b = input("Give me another number: ")
    a = int(a)
    b = int(b)
    print(a / b)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
