# Check if input text starts with a user-given prefix
text = input("Enter a string: ")
prefix = input("Enter a prefix: ")
print("Result:", text[:len(prefix)] == prefix)
