# Get input
text = input("Enter a string: ")
width = int(input("Enter width: "))

# Add spaces to the right
if len(text) < width:
    text += ' ' * (width - len(text))

# Print result
print("Left-justified:", text)
