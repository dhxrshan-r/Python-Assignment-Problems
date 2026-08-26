def print_board(board):
    for row in board:
        result = ""
        for value in row:
            result = result + value
        print(result)

game_board = [ [ "X", " ", "O" ],
               [ " ", "X", " " ],
               [ " ", " ", "O" ] ]
print_board(game_board)