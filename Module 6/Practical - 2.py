def in_increasing_order(words):
    max_len = len(words)
    for i in range(max_len - 1):
        if not len(words[i]) <= len(words[i + 1]):
            return False
    return True
print(in_increasing_order(["a","at", "cat", "and", "fort"]))