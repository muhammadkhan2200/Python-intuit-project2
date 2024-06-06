# Define the function
def calculate_perimeter(length, width):
    # Calculate the perimeter
    perimeter = 2 * (length + width)
    # Return the perimeter
    return perimeter

# Call the function with length and width
length = 5
width = 3
result = calculate_perimeter(length, width)
print(f"The perimeter of the rectangle with length {length} and width {width} is {result}.")