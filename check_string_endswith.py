# Initialize function to check if a string ends with a given suffix
def check_string_endswith(s, suffix):
    return s[-len(suffix):] == suffix if len(suffix) <= len(s) else False


s = "hello.txt"
suffix = ".txt"
print("Does", repr(s), "end with", repr(suffix), "?", check_string_endswith(s, suffix))

