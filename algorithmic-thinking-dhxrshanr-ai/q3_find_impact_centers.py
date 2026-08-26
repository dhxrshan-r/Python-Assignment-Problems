""" Question 3: find_impact_centers """
"""
Input: 2D list of 0s and 1s representing electrical activity in an area
Output: List of [row, col]s where lightning directly struck
"""
def find_impact_centers(board):
    result = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            count=0
            if board[i][j] == 1:
                #left
                if j-1 < 0 or board[i][j-1]==1:
                    count+=1
                # right
                if j+1>=len(board[i]) or board[i][j+1]==1:
                    count+=1
                #top
                if i-1 < 0 or board[i-1][j]==1:
                    count+=1
                #down
                if i+1>=len(board) or board[i+1][j]==1:
                    count+=1

                if count==4:
                    result.append([i,j])            
    return result

""" Test 3 """
def test_find_impact_centers():
    print("Testing find_impact_centers...", end="")
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
    print("... done!")
test_find_impact_centers()

