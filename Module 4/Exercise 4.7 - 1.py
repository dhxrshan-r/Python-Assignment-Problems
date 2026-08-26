def is_vowel(c):
    for vowel in "aeiouAEIOU":
        if c == vowel:
            return True
    return False

def count_vowels(s):
    count = 0
    return count_vowel_helper(s,count)
    
def count_vowel_helper(s,count):
    if s == "":
        return count
    else:
        if (is_vowel(s[0])):
            partial_result = count_vowel_helper(s[1:], count + 1)
        else:
           partial_result = count_vowel_helper(s[1:], count)
        return partial_result
 

print("Testing count_vowels...", end = "")
assert(count_vowels("hello") == 2)
assert(count_vowels("apple") == 2)
assert(count_vowels("How are you doing today?") == 9)
assert(count_vowels("aeiou") == 5)
assert(count_vowels("AEIOU") == 5)
assert(count_vowels("why?") == 0)
assert(count_vowels("") == 0)
print("...done")