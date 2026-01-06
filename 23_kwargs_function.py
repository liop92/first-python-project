def display_profile(**kwargs):
    print("Profile Information: ")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_profile(name="Mike", age=35, city="London", job="Graphic Designer")
