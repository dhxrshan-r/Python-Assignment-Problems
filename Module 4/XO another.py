def combine_values(row):
    result = ""
    for value in row:
        result = result + value
    return result

def print_board(board):
    for row in board:
        print(combine_values(row))

game_board = [ [ "X", " ", "O" ],
               [ " ", "X", " " ],
               [ " ", " ", "O" ] ]
print_board(game_board)