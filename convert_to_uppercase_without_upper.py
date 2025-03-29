# Get a string from the user
def convert_to_uppercase_without_upper(text):  
    # Convert each lowercase letter to uppercase using ASCII values  
    result = ""
    for char in text:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Return the uppercase string
