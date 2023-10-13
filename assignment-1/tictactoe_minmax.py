# Initialize an empty 3x3 game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if the game is over (win or tie)
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check for a tie
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Tie'
    return None

# Function to make a player's move
def make_move(player, board):
    while True:
        try:
            row, col = map(int, input(f"Enter row and column (0-2) for player {player} (e.g., 0 1): ").split())
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column.")

# Function to simulate the bot's move using minimax
def bot_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # Assume the bot's move
                score = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        board[best_move[0]][best_move[1]] = 'O'  # Make the best move for the bot

# Minimax algorithm to evaluate the game state
def minimax(board, depth, is_maximizing):
    result = is_game_over(board)
    if result == 'X':
        return -1
    if result == 'O':
        return 1
    if result == 'Tie':
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

while True:
    print_board(board)
    make_move('X', board)

    result = is_game_over(board)
    if result:
        print_board(board)
        if result == 'Tie':
            print("It's a tie!")
        else:
            print(f"Player {result} wins!")
        break

    bot_move(board)

    result = is_game_over(board)
    if result:
        print_board(board)
        if result == 'Tie':
            print("It's a tie!")
        else:
            print(f"Player {result} wins!")
        break