# Initialize function for centering a string
def center_align_string(s, width):
    total_spaces = max(0, width - len(s))
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return " " * left_spaces + s + " " * right_spaces


s = "Center"
print("Original:", repr(s))
print("After centering (width 10):", repr(center_align_string(s, 10)))
