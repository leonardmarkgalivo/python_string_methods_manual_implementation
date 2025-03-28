# Initialize function to check if all characters are uppercase
def check_all_uppercase(s):
    for char in s:
        if "a" <= char <= "z":
            return False
    return True if s else False

s1 = "HELLO"
s2 = "Hello"
print("Is", repr(s1), "all uppercase?", check_all_uppercase(s1))
print("Is", repr(s2), "all uppercase?", check_all_uppercase(s2))
