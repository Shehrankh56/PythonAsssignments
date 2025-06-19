def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose your move (1-9): ")
        
        # Validate input
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid move. Try again.")
            continue
        
        move = int(move) - 1
        row, col = move // 3, move % 3
        
        if board[row][col] in ['X', 'O']:
            print("That spot is already taken. Try again.")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
