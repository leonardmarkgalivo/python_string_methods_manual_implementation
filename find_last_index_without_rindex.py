# Get input text and substring, then find last index
text = input("Enter a string: ")
substring = input("Enter substring to find: ")
index = next((i for i in range(len(text) - len(substring), -1, -1) if text[i:i + len(substring)] == substring), -1)
print("Result:", index)


