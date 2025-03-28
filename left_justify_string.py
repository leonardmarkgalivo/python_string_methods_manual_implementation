# Initialize function for left-justifying a string
def left_justify_string(s, width):
    return s + " " * (width - len(s)) if len(s) < width else s


s = "Align"
print("Original:", repr(s))
print("After left-justifying (width 10):", repr(left_justify_string(s, 10)))
