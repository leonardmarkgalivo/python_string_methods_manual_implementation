# Get input
text = input("Enter a string: ")

# Find first non-space character
i = 0
while i < len(text) and text[i] == ' ':
    i += 1

# Print trimmed string
print("Trimmed:", text[i:])
