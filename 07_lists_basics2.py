movies_list = []

for i in range(1, 6):
    movie = input(f"Enter favorite movie #{i}: ")
    movies_list.append(movie.title())

movies_list.sort()

movies_string = ", ".join(movies_list)

print(f"Your top 5 movies are: {movies_string}.")
