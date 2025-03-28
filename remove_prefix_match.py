# Get input
text = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")

# Remove prefix if it matches
if text.startswith(prefix):
    text = text[len(prefix):]

# Print result
print("Result:", text)
