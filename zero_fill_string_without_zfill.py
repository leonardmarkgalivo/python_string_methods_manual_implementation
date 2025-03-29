# Get a string and a total width
def zero_fill_string_without_zfill(text, width):  
    # Add zeros before the string to reach the required width  
    return "0" * (width - len(text)) + text if len(text) < width else text

# Return the zero-filled string
