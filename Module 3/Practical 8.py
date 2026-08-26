def is_lower(s):
    if len(s) == 0:
        return False
    has_lowercase = False
    for c in s:
        if "A" <= c <= "Z":
            return False
        if "a" <= c <= "z":
            has_lowercase = True
            
    return has_lowercase
print(is_lower("Hello23"))
