# Initialize function to convert string to title case
def convert_to_title_case(s):
    words = s.split()
    result = []
    for word in words:
        first_char = word[0].upper() if "a" <= word[0] <= "z" else word[0]
        rest = "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in word[1:])
        result.append(first_char + rest)
    return " ".join(result)


s = "hello world from python"
print("Original:", repr(s))
print("After converting to title case:", repr(convert_to_title_case(s)))
