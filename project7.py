
def calculate_volume(length, width, height=1):
    # Calculate the volume
    volume = length * width * height
    # Return the volume
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