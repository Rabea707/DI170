#Mini-Project - Tic Tac Toe
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player1 = "X"
player2 = "O"

def display_board(board):
    print()
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()

def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (0-2): "))
            col = int(input(f"Player {player} - Enter col (0-2): "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if row < 0 or row > 2:
            print("Row must be between 0 and 2")
            continue

        if col < 0 or col > 2:
            print("Col must be between 0 and 2")
            continue

        if board[row][col] != " ":
            print("This cell is already taken")
            continue

        return row, col


def check_win(board, player):
    # rows
    if board[0][0] == player and board[0][1] == player and board[0][2] == player: return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player: return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player: return True

    # cols
    if board[0][0] == player and board[1][0] == player and board[2][0] == player: return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player: return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player: return True

    # diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    current_player = player1

    while True:
        display_board(board)

        row, col = player_input(current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
play()
