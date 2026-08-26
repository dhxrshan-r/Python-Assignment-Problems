def is_alpha_num(s):
    if len(s) == 0:
        return False
    for c in s:
        if not (("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")):
            return False
    return True
print(is_alpha_num("1234"))
print(is_alpha_num("Hello"))
print(is_alpha_num("1234Hello"))