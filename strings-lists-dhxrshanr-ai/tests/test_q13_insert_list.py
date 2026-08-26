from q13_insert_list import insert_list 

def test_insert_list():
    L = [1, 5, 6]
    K = [2, 3, 4]
    assert(insert_list(L, 1, K) == None)
    assert(L == [1, 2, 3, 4, 5, 6])
    L1 = [2, 4]
    K1 = [5, 1, 8]
    assert(insert_list(L1, 2, K1) == None)
    assert(L1 == [2, 4, 5, 1, 8])
    
