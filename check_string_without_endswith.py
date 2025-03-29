# Get input
text = input("Enter a string: ")
suffix = input("Enter suffix to check: ")

# Check if string ends with suffix
ends = text[-len(suffix):] == suffix if len(suffix) <= len(text) else False

# Print result
print("Ends with suffix?", ends)
