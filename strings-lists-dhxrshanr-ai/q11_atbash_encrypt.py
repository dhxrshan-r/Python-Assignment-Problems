""" Question 11: atbash_encrypt """
"""
Input: string
Output: string encoded using atbash encryption
"""
import string
def atbash_encrypt(message):
    alphabets = string.ascii_lowercase
    rev = alphabets[::-1]
    enc = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                idx = alphabets.index(c.lower())
                enc += rev[idx].upper()
            else:
                idx = alphabets.index(c)
                enc += rev[idx]
        else:
            enc += c
    return enc

""" Test 11 """
def test_atbash_encrypt():
    print("Testing atbash_encrypt...", end='')
    assert(atbash_encrypt("Hello") == "Svool")
    assert(atbash_encrypt("night!") == "mrtsg!")
    assert(atbash_encrypt("Coding is fun :)") == "Xlwrmt rh ufm :)")
    assert(atbash_encrypt("") == "")
    print("... done!")

if __name__ == '__main__':
    test_atbash_encrypt()