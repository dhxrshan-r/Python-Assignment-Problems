from q3_intersect import intersect 

def test_intersect():
    L = [1, 2, 2, 3, 0]
    K = [1, 1, 2, 5, 0]
    assert(intersect(L, K) == [1, 1, 2, 0])
    L1 = [6, 7, 8, 9]
    K1 = [2, 7, 7, 7, 5]
    assert(intersect(L1, K1) == [7, 7, 7])
    
    # if your code is failing this test, check the efficiency!
    L2 = [0]*30000
    K2 = [0]*30000
    assert(intersect(L2, K2) == [0]*30000)
   

