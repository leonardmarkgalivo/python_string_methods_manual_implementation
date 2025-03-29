# Get a string and a total width
def right_justify_string_without_rjust(text, width):  
    # Add spaces before the string to reach the required width  
    return " " * (width - len(text)) + text if len(text) < width else text

# Return the justified string
