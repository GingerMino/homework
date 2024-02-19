numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def func(number):
    return number % 2 != 0 and number > 50

print(list(filter(func, numbers)))