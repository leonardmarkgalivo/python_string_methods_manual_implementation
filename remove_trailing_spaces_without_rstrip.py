def remove_trailing_spaces_without_rstrip(text):  
    # Iterate from the end to find the first non-space character  
    i = len(text) - 1
    while i >= 0 and text[i] == " ":
        i -= 1
    return text[:i + 1]
