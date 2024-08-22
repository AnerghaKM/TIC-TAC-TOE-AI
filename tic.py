import math

# Define the board
board = [' ' for _ in range(9)]  # 3x3 Tic-Tac-Toe board

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a win
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a draw
def check_draw(board):
    return ' ' not in board

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Determine the best move
def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    print_board(board)
    while True:
        # Human move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[human_move] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print("AI chose position", ai_move + 1)
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

play_game()
