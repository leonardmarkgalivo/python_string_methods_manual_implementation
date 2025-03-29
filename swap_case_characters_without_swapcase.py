# Get input
text = input("Enter a string: ")

# Swap case
swapped = ""
for char in text:
    if 'a' <= char <= 'z':
        swapped += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        swapped += chr(ord(char) + 32)
    else:
        swapped += char

# Print result
print("Swapped case:", swapped)
