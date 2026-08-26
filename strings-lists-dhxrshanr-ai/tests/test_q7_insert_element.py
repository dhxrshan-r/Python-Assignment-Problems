from q7_insert_element import insert_element

def test_insert_element():
    L = [1, 2, 3, 4]
    assert(insert_element(L, 1, 5) == None)
    assert(L == [1, 5, 2, 3, 4])
    L1 = [2, 4, 6]
    assert(insert_element(L1, 5, 0) == None)
    assert(L1 == [2, 4, 6, 0])
    L2 = []
    assert(insert_element(L2, 0, 5) == None)
    assert(L2 == [5])
    
