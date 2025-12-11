n = int(input("Give me a number: "))

# 1. Even numbers 0 → n
for x in range(n + 1):
    if x % 2 == 0:
        print(x)

print()

# 2. Countdown n → 0
for x in range(n, -1, -1):
    print(x)

print()

# 3. Square list
square_list = [x ** 2 for x in range(1, n + 1)]
print(f"The square list is: {square_list}")

print()

# 4. Search for 13
for x in range(1, n + 1):
    if x == 13:
        print("Unlucky 13 found!")
        break
    print(x)
