# Initialize function for removing prefix if it matches
def remove_prefix_match(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    return s

s = "unhappy"
prefix = "un"
print("Original:", repr(s))
print("After removing prefix:", repr(remove_prefix_match(s, prefix)))
