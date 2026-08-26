from q2_ends_with import ends_with 

def test_ends_with():
    assert(ends_with("Hello world", "world") == True)
    assert(ends_with("Hello world", "rld") == True)
    assert(ends_with("rain", "r") == False)
    assert(ends_with("apple", "") == True)
    assert(ends_with("", "abc") == False)
   
