def sum_numbers(*args):
    suma = 0
    for num in args:
        suma += num
    return suma


print(sum_numbers(1, 2, 3, 4, 5))
