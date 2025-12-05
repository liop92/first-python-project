first_movie = input("What is your first favorite movie?: ")
second_movie = input("What is your second favorite movie?: ")
third_movie = input("What is your third favorite movie?: ")
forth_movie = input("What is your forth favorite movie?: ")
fift_movie = input("What is your fift favorite movie?: ")

movies_list = [first_movie.title(), second_movie.title(
), third_movie.title(), forth_movie.title(), fift_movie.title()]

movies_list.sort()

print(f"Your top 5 movies are: {movies_list}")
