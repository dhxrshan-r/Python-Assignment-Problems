from q1_starts_with import starts_with 


def test_starts_with():
    assert(starts_with("Hello world", "Hello", 0) == True)
    assert(starts_with("Hello world", "Hello", 3) == False)
    assert(starts_with("butterfly", "fly", 4) == False)
    assert(starts_with("butterfly", "fly", 6) == True)
    assert(starts_with("orange", "", 4) == True)
    assert(starts_with("", "abc", 0) == False)
    
