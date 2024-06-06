def greet_user(username):
    print(f"Hello, {username} Welcome to Python Functions.")

# Call the function with a username
greet_user("John Doe")

# Define the function
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# Call the function with length and width
length = 5
width = 3
result = calculate_perimeter(length, width)
print(f"The perimeter of the rectangle with length {length} and width {width} is {result}.")

# Define the function
def calculate_volume(length, width, height=1):
    volume = length * width * height
    return volume

# Call the function with length, width, and height
length = 5
width = 3
height = 2
result = calculate_volume(length, width, height)
print(f"The volume of the rectangular prism with length {length}, width {width}, and height {height} is {result}.")

# Call the function with length and width (using default height)
length = 5
width = 3
result = calculate_volume(length, width)
print(f"The volume of the rectangular prism with length {length}, width {width}, and default height is {result}.")

# Define the function
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Call the function with an even number
number = 10
result = is_even(number)
print(f"The number {number} is even: {result}.")

# Call the function with an odd number
number = 11
result = is_even(number)
print(f"The number {number} is even: {result}.")