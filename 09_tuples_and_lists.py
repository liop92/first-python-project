cities_tuple = ("Bucharest", "Tokyo", "London", "Paris", "Berlin")

print(f"\nThe first city is: {cities_tuple[0]}")
print(f"The last city is: {cities_tuple[-1]}")
print(f"The first three cities are: {cities_tuple[:3]}")

cities_list = list(cities_tuple)

cities_list.append("Helsinki")
print("\nList after adding a city:")
print(cities_list)

if "Bucharest" in cities_list:
    cities_list.remove("Bucharest")
print("\nList after removing Bucharest:")
print(cities_list)

cities_tuple = tuple(cities_list)
print("\nFinal tuple:")
print(cities_tuple)
