from q11_atbash_encrypt import atbash_encrypt

def test_atbash_encrypt():
    assert(atbash_encrypt("Hello") == "Svool")
    assert(atbash_encrypt("night!") == "mrtsg!")
    assert(atbash_encrypt("Coding is fun :)") == "Xlwrmt rh ufm :)")
    assert(atbash_encrypt("") == "")
    
