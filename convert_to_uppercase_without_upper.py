# Convert input text to uppercase manually
text = input("Enter a string: ")
result = ""
for char in text:
    result += chr(ord(char) - 32) if "a" <= char <= "z" else char
print("Result:", result)



