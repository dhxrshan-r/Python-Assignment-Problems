from q12_merge import merge

def test_merge():
    
    L1 = [1, 3, 5]
    L2 = [2, 4, 6]
    assert(merge(L1, L2) == [1, 2, 3, 4, 5, 6])
    assert(L1 == [1, 3, 5])
    assert(L2 == [2, 4, 6])
    assert(merge([1, 2, 5], [4, 6, 7]) == [1, 2, 4, 5, 6, 7])
    
