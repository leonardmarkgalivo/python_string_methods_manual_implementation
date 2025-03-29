# Get input and remove spaces from the end
text = input("Enter a string: ")
i = len(text) - 1
while i >= 0 and text[i] == " ":
    i -= 1
print("Result:", text[:i + 1])

