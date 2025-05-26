# Define a function to calculate  area of a rectangle
def calculate_area(length, width):
    return length * width

# Take user input for length  width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call  function and store the result
area = calculate_area(length, width)

# Print  result
print(f"The area of the rectangle is: {area}")
