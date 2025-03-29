# Get a string and a substring to find
def find_first_index_without_index(text, substring):  
    # Find the first occurrence of the substring in the string  
    for i in range(len(text) - len(substring) + 1):
        if text[i:i + len(substring)] == substring:
            return i
    return -1
