age = int(input("What is your age?: "))

if age < 0:
    print("Age cannot be negative!")

elif age < 18:
    print("You cannot drive.")

else:
    print("You are an adult.")
    has_license = input("Do you have a driving license? (yes/no): ").lower()

    if has_license == "no":
        print("You are old enough, but you don't have a license.")

    elif has_license == "yes":
        category = input("What category? (A/B/C): ").upper()

        if category == "A":
            print("You can drive motorcycles.")
        elif category == "B":
            print("You can drive a car.")
        elif category == "C":
            print("You can drive trucks.")
        else:
            print("Invalid category.")
