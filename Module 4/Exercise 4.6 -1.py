def is_vowel(c):
    for vowel in "aeiouAEIOU":
        if c == vowel:
            return True
    return False


def get_vowels(s):
    if s == "":
        return ""
    else:
        left_over_string = s[0]
        smaller_string = s[1:]
        partial_result = get_vowels(smaller_string)
        if is_vowel(s[0]):
            return left_over_string + partial_result
        else:
            return partial_result

print(get_vowels("Apple"))
