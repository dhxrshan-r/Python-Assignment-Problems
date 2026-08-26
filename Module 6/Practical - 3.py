board = [ [ 0, 0, 0, 0, 1 ],
          [ 0, 1, 0, 1, 1 ],
          [ 1, 1, 1, 0, 1 ],
          [ 0, 1, 1, 0, 0 ],
          [ 0, 1, 1, 1, 0 ] ]

def find_impact_centers(board):
    result = []
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] == 0:
                continue
            count = 0
            if col - 1 < 0 or board[row][col - 1] == 1:
                count += 1
            if col + 1 >= len(board[row]) or board[row][col + 1] == 1:
                count += 1
            if row - 1 < 0 or board[row - 1][col] == 1:
                count += 1
            if row + 1 >= len(board) or board[row + 1][col] == 1:
                count += 1
            if count == 4:
                result.append([row, col])
    return result
print(find_impact_centers(board))