def is_alpha(s):
    if len(s) == 0:
        return False
    for c in s:
        if not (("a" <= c <= "z") or ("A" <= c <= "Z")):
            return False
    return True
print(is_alpha("1234"))
print(is_alpha("Hello"))