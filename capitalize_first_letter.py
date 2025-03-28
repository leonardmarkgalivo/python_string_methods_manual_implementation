# Get input
text = input("Enter a string: ")

# Capitalize first letter
if text:
    text = text[0].upper() + text[1:].lower()

# Print result
print("Capitalized:", text)
