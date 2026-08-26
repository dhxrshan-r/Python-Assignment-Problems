def is_digits(s):
    if len(s) == 0:
        return False
    for c in s:
        if not ("0" <= c <= "9"):
            return False
    return True
print(is_digits("1234"))
