# Get a string from the user
def check_all_lowercase_without_islower(text):  
    # Check if all characters in the string are lowercase  
    for char in text:
        if "A" <= char <= "Z":
            return False
    return True if text else False

# If found, return False; otherwise, return True
