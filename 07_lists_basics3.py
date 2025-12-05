food_list = []


for i in range(1, 6):
    food = input(f"Enter favorite food #{i}: ")
    food_list.append(food.title())


print("\nFirst food:", food_list[0])
print("Last food:", food_list[-1])
print("First 3 foods:", food_list[:3])
print("Reversed list:", food_list[::-1])


food_list.append("French Fries")

if "Roast Chicken" in food_list:
    food_list.remove("Roast Chicken")


food_list.sort()


food_string = ", ".join(food_list)
print("\nYour favorite foods after adding/removing/sorting:", food_string)
