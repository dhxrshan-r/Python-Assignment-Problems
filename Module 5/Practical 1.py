def starts_with(s, t, start):
    if s[start :start+ len(t)] == t:
        return True
    return False

print (starts_with("butterfly","fly",6))