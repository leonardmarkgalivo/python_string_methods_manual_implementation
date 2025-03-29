# Get input text and suffix, then remove if present
text = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")
if text.endswith(suffix):
    text = text[:-len(suffix)]
print("Result:", text)


