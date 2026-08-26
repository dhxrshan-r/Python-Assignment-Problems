from q4_count import count 

def test_count():
    assert(count("Hello", "l") == 2)
    assert(count("pineapple", "p") == 3)
    assert(count("farewell everyone", "are") == 1)
    assert(count("", "aa") == 0)
    assert(count("Hello world", " ") == 1)
