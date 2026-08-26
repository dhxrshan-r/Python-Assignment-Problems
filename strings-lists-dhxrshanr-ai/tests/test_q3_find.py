from q3_find import find 

def test_find():
    
    assert(find("Hello", "ello", 0) == 1)
    assert(find("Hello world", "wor", 2) == 6)
    assert(find("goodbye", "bye", 5) == -1)
    assert(find("goodbye", "bye", 1) == 4)
    assert(find("rainbow", "rainbow", 0) == 0)
    assert(find("", "x", 0) == -1)
    
