# Get a string and a prefix
def check_string_startswith_without_startswith(text, prefix):  
    # Compare the beginning of the string with the prefix  
    return text[:len(prefix)] == prefix if len(prefix) <= len(text) else False

# Return True if they match, otherwise return False
