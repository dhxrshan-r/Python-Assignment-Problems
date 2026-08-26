def longest_string_length(s):
    if not s:
        return 0
    count = 0
    for string in s:
        if len(string) > count:
            count = len(string)
    return count
print(longest_string_length(["hello", "world", "python", "programming"]))
