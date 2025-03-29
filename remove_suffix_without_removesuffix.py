# Get a string and a suffix to remove
def remove_suffix_without_removesuffix(text, suffix):  
    # Check if the string ends with the given suffix and remove it  
    if text[-len(suffix):] == suffix and len(suffix) <= len(text):
        return text[:-len(suffix)]
    return text

