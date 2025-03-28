# Get input
text = input("Enter a string: ")

# Check if all letters are uppercase
is_upper = True
for char in text:
    if 'a' <= char <= 'z':
        is_upper = False
        break

# Print result
print("Is all uppercase?", is_upper)
