# Initialize function to capitalize the first letter
def capitalize_first_letter(s):
    if not s:
        return s
    first_char = s[0].upper() if "a" <= s[0] <= "z" else s[0]
    rest = "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s[1:])
    return first_char + rest


s = "hELLO world"
print("Original:", repr(s))
print("After capitalizing first letter:", repr(capitalize_first_letter(s)))
