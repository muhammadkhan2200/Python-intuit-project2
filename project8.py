def is_even(number):
    # Check if the number is even
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