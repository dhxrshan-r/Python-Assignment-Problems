def is_vowel(c):
    for vowel in "aeiouAEIOU":
        if c == vowel:
            return True
    return False

def count_vowels(s):
    if s == "":
        return 0
    else:
        smaller_string = s[1:]
        partial_result = count_vowels(smaller_string)
        if is_vowel(s[0]):
            return partial_result + 1
        else:
            return partial_result
print(count_vowels("hannah"))
        