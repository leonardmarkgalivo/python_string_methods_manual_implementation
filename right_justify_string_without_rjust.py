# Get input text and width, then right justify
text = input("Enter a string: ")
width = int(input("Enter width: "))
print("Result:", " " * (width - len(text)) + text if len(text) < width else text)


