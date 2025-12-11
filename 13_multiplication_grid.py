n = int(input("Give a number: "))

for i in range(0, n):
    for j in range(0, n):
        x = i * j
        print(x, end=" ")
    print()
