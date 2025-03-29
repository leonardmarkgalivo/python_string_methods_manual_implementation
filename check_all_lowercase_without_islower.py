# Check if input text is fully lowercase
text = input("Enter a string: ")
is_lower = all("a" <= char <= "z" or not char.isalpha() for char in text)
print("Result:", is_lower)



