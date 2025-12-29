# Tic Tac Toe (2 players) - Terminal version

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]  # "X" or "O"
    return None

def is_draw(board):
    return " " not in board

def get_move(player, board):
    while True:
        move = input(f"Player {player}, choose a position (1-9): ").strip()

        if not move.isdigit():
            print("Type a number from 1 to 9.")
            continue

        pos = int(move) - 1  # convert 1-9 to 0-8

        if pos < 0 or pos > 8:
            print("Pick a number from 1 to 9.")
            continue

        if board[pos] != " ":
            print("That spot is taken. Choose another.")
            continue

        return pos

def play():
    board = [" "] * 9
    player = "X"

    print("Tic Tac Toe!")
    print("Positions are like this:")
    demo = ["1","2","3","4","5","6","7","8","9"]
    print_board(demo)

    while True:
        print_board(board)

        pos = get_move(player, board)
        board[pos] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play()
