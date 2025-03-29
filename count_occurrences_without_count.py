# Get input text and substring, then count occurrences
text = input("Enter a string: ")
substring = input("Enter substring to count: ")
count = sum(1 for i in range(len(text) - len(substring) + 1) if text[i:i + len(substring)] == substring)
print("Result:", count)


