# method 1
def square_sum(numbers):
    sum = 0
    for i in numbers:
         sum = sum + i**2
    return sum

# method 2
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

# method 3
def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))

# method 4
def square_sum(numbers):
    return sum([x**2 for x in numbers])