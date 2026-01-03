counter_1 = 0


def increment_1():
    global counter_1
    counter_1 += 1
    print(counter_1)


increment_1()
increment_1()
increment_1()
print(counter_1)

print("---AND---")

counter_2 = 0


def increment_2():
    global counter_2
    counter_2 += 1


increment_2()
increment_2()
increment_2()
print(counter_2)
