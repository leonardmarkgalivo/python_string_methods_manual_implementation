# Get a string and a substring to count
def count_occurrences_without_count(text, substring):  
    # Count how many times the substring appears in the string  
    count = 0
    for i in range(len(text) - len(substring) + 1):
        if text[i:i + len(substring)] == substring:
            count += 1
    return count

