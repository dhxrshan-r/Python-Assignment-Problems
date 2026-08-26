from q3_find_impact_centers import find_impact_centers 


def test_find_impact_centers():
    data1 = [ [ 0, 0, 0, 0, 1 ],
              [ 0, 1, 0, 1, 1 ],
              [ 1, 1, 1, 0, 1 ],
              [ 0, 1, 1, 0, 0 ],
              [ 0, 1, 1, 1, 0 ] ]
    assert(sorted(find_impact_centers(data1)) == [ [1, 4], [2, 1], [4, 2] ])
    data2 = [ [ 1, 0, 0],
              [ 0, 0, 0],
              [ 0, 1, 0] ]
    assert(sorted(find_impact_centers(data2)) == [ ])
    data3 = [ [ 1, 1, 1, 1 ],
              [ 1, 1, 1, 1 ],
              [ 1, 1, 1, 1 ],
              [ 1, 0, 0, 1 ] ]
    assert(sorted(find_impact_centers(data3)) == [ [0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3] ])


