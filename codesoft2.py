import math

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initial board setup
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

def evaluate(board):
    # Check rows for victory
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == AI:
                return 10
            elif row[0] == HUMAN:
                return -10

    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == AI:
                return 10
            elif board[0][col] == HUMAN:
                return -10

    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == AI:
            return 10
        elif board[0][0] == HUMAN:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == AI:
            return 10
        elif board[0][2] == HUMAN:
            return -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = EMPTY
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def is_winner(board, player):
    return evaluate(board) == (10 if player == AI else -10)

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if not is_moves_left(board) or is_winner(board, HUMAN) or is_winner(board, AI):
            break

        # Human move
        while True:
            try:
                row, col = map(int, input("Enter row and column (1-3) separated by a space: ").split())
                row, col = row - 1, col - 1
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("This cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 1 and 3.")

        print_board(board)

        if is_winner(board, HUMAN):
            print("Congratulations! You won!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's move:")
        row, col = find_best_move(board)
        board[row][col] = AI
        print_board(board)

        if is_winner(board, AI):
            print("AI wins! Better luck next time.")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

play_game()
