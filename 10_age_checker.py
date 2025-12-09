age = int(input("What is your age?: "))

if age < 0:
    print("Age cannot be negative!")
elif age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")
