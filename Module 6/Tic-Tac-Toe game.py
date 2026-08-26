"""
Make a board
Display the board
Set player_1_turn to True
While game is not over
    if player_1_turn is True
        Have player 1 take their turn
    Otherwise
        Have player 2 take their turn
    Display the board
    Set player_1_turn to the opposite
"""

def play_game():
    board = make_board()
    show_board(board)
    player_1_turn = True
    while not is_game_over(board):
        if player_1_turn == True:
            take_turn(board, "X")
        else:
            take_turn(board, "O")
        show_board(board)
        player_1_turn = not player_1_turn

def make_board():
    size = 3
    board = []
    for row in range(size):
        board.append([ " " ] * size)
    return board

def show_board(board):
    for row in board:
        s = ""
        for letter in row:
            s += letter
        print(s)

def take_turn(board, player):
    while True:
        row = input("Enter a row:")
        col = input("Enter a col:")
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            if (0 <= row < len(board)) and (0 <= col < len(board[0])):
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("That spot isn't open, try again.")
            else:
                print("Not on the board, try again.")
        else:
            print("That's not a number! Try again!")

# Test: 3, 2 [out of bounds]
# Test: 1, -1 [out of bounds]
# Test: 1, 2 with board will have O at 1,2 [already placed]
# Test: foo, bar [non-numbers]

"""
Check if any of the rows have three Xs or three Os, if so, game is over
Check if any of the cols have three Xs or three Os, if so, game is over
Check if any of the diagonals have three Xs or three Os, if so, game is over
Otherwise
    If the board contains a space, the game is NOT over
    Otherwise, the game is over
"""

def is_game_over(board):
    combos = get_rows(board) + get_cols(board) + get_diags(board)
    for combo in combos:
        if combo == "X" * len(board) or combo == "O" * len(board):
            return True

    if contains_space(board):
        return False
    else:
        return True 

def get_rows(board):
    rows = []
    for row in board:
        combo = ""
        for letter in row:
            combo += letter
        rows.append(combo)
    return rows

def get_cols(board):
    cols = []
    for col_index in range(len(board)):
        combo = ""
        for row in board:
            combo += row[col_index]
        cols.append(combo)
    return cols

def get_diags(board):
    diag_1 = ""
    diag_2 = ""
    for i in range(len(board)):
        diag_1 += board[i][i]
        diag_2 += board[i][len(board)-1 - i]
    return [diag_1, diag_2]

def contains_space(board):
    for row in board:
        for value in row:
            if value == " ":
                return True
    return False

def test_make_board():
    assert(make_board() == [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ])

def test_show_board():
    board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
    show_board(board)
    # is it an empty board?

    board = [ ["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"] ]
    show_board(board)
    # does it have the right pattern?

def test_is_game_over():
    board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
    assert(is_game_over(board) == False)
    board = [ ["X", " ", "O"], ["O", "X", "X"], [" ", "X", "O"] ]
    assert(is_game_over(board) == False)
    board = [ ["X", " ", "O"], ["O", "X", "O"], [" ", "X", "X"] ]
    assert(is_game_over(board) == True)
    board = [ ["X", " ", "O"], ["X", "X", "O"], [" ", "X", "O"] ]
    assert(is_game_over(board) == True)
    board = [ ["X", "O", "O"], ["O", "X", "X"], ["X", "X", "O"] ]
    assert(is_game_over(board) == True)
print (play_game())