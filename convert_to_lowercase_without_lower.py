# Get input
text = input("Enter a string: ")

# Convert to lowercase
lower_text = ""
for char in text:
    if 'A' <= char <= 'Z':
        lower_text += chr(ord(char) + 32)
    else:
        lower_text += char

# Print result
print("Lowercase:", lower_text)
