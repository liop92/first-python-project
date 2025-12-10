password = input("Tell me a password and I'll check its strength: ")

length = len(password)
has_letter = any(char.isalpha() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in "!@#$%^&*()?" for char in password)

if length < 6:
    print("The password is very weak.")

elif 6 <= length <= 10 and (has_letter or has_digit):
    print("The password is weak.")

elif length > 10 and has_letter and has_digit and not has_symbol:
    print("Your password is medium strength.")

elif length > 10 and has_letter and has_digit and has_symbol:
    print("Your password is strong.")

else:
    print("The password does not match any category.")
