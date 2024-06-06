 # Function to Calculate the Area of a Circle

import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = math.pi * (radius ** 2)
        return area

# Call the function
radius = 5
result = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {result:.2f}.")

 # Function to Check if a Number is a Prime Number

def is_prime_number(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Call the function
number = 23
result = is_prime_number(number)
print(f"The number {number} is a prime number: {result}.")

 # Function to Calculate the Average of a List of Numbers

def calculate_average(numbers):
    if len(numbers) == 0:
        return "List is empty."
    else:
        total = sum(numbers)
        average = total / len(numbers)
        return average

# Call the function
numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print(f"The average of the list {numbers} is {result:.2f}.")