from q5_count import count 

def test_strip():
    assert(strip("Hello") == "Hello") 
    assert(strip(" Hello world ") == "Hello world") 
    assert(strip("      apple ") == "apple") 
    assert(strip("    ") == "") 
    
