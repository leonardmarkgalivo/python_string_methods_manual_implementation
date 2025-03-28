# Get input
text = input("Enter a string: ")

# Convert to title case
words = text.split()
title_case = ""
for word in words:
    title_case += word[0].upper() + word[1:].lower() + " "

# Print result
print("Title case:", title_case.strip())
