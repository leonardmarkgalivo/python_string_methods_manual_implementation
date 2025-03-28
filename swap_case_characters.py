# Initialize function to swap case of each character
def swap_case_characters(s):
    result = ""
    for char in s:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        elif "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
            result += char
    return result


s = "HeLLo WoRLd!"
print("Original:", repr(s))
print("After swapping case:", repr(swap_case_characters(s)))

