# Get input
text = input("Enter a string: ")
width = int(input("Enter width: "))

# Calculate left and right spaces
left_spaces = (width - len(text)) // 2
right_spaces = width - len(text) - left_spaces

# Print result
print("Centered:", ' ' * left_spaces + text + ' ' * right_spaces)
