# Initialize function for removing leading spaces
def remove_leading_spaces(s):
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    return s[i:]


s = "   Hello, World!"
print("Original:", repr(s))
print("After removing leading spaces:", repr(remove_leading_spaces(s)))
