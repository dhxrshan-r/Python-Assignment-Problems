def all_evens(s):
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    return result
print(all_evens("abcdefgh"))
