# Get a string and a substring to find
def find_last_index_without_rindex(text, substring):  
    # Find the last occurrence of the substring in the string  
    for i in range(len(text) - len(substring), -1, -1):
        if text[i:i + len(substring)] == substring:
            return i
    return -1

