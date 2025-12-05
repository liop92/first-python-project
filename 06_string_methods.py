full_name = input("What is your full name?: ")
country = input("What country are you from?: ")
hobby = input("What is your favorite hobby?: ")

print(f"FULL NAME: {full_name.upper()}")
print(f"Country: {country.title()}")
print(f"Hobby: {hobby.lower()}")

print(
    f"Hello, {full_name.upper()}! You live in {country.title()} and your hobby is {hobby.lower()}.")
