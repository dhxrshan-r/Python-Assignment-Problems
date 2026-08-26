from q7_index_range import index_range 

def test_index_range():
    assert(index_range([1, 1, 2, 3, 3, 3], 1) == [0, 1])
    assert(index_range([1, 1, 2, 3, 3, 3], 2) == [2, 2])
    assert(index_range([1, 1, 2, 3, 3, 3], 3) == [3, 5])
    assert(index_range([1, 1, 2, 3, 3, 3], 4) == [-1, -1])
   

