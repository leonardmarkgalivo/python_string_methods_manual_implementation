# Initialize function for converting string to lowercase
def convert_to_lowercase(s):
    result = ""
    for char in s:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


s = "HeLLo WORLD"
print("Original:", repr(s))
print("After converting to lowercase:", repr(convert_to_lowercase(s)))
