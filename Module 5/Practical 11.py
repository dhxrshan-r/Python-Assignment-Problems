import string

def atbash_encrypt(message):
    result = ""
    for c in message:
        result += shift(c)
    return result

def shift(c):
    if not c.isalpha():
        return c
    if c.islower():
        alpha = string.ascii_lowercase
    else:
        alpha = string.ascii_uppercase
    reverse_alpha = alpha[::-1]
    return reverse_alpha(alpha.find(c))