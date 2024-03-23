print("Tic-Tac-Toe by Mansi\n")

# Initialize the Tic-Tac-Toe board
board = [[" 🔮 ", " 🔮 ", " 🔮 "],[" 🔮 ", " 🔮 ", " 🔮 "],[" 🔮 ", " 🔮 ", " 🔮 "]]

# Display the initial state of the board
for row in board:
    print("".join(row))

# Function to check for a winning condition
def check_result(symbol):
    symbol_count = 0
    for row in board:
        for element in row:
            if element == symbol:
                symbol_count += 1
    if symbol_count >= 3:
        # Check for winning conditions: diagonal, row, or column
        #diagonal cut
        if board[0][0] == board[1][1] == board[2][2] == symbol:
            board[0][0] = board[1][1] = board[2][2] = f"_{symbol.strip()}_"
            return True
        if board[0][2] == board[1][1] == board[2][0] == symbol:
            board[0][2] = board[1][1] = board[2][0] = f"_{symbol.strip()}_"
            return True
        #row cut
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == symbol:
                board[i][0] = board[i][1] = board[i][2] = f"_{symbol.strip()}_"
                return True
        #column cut
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == symbol:
                board[0][j] = board[1][j] = board[2][j] = f"_{symbol.strip()}_"
                return True
    return False

# Function for a player's turn

def player_turn(symbol):
    try:
        # Get player input for row and column
        player_row = int(input(f"\nPlayer{symbol.strip()}: Enter row? (0, 1, 2)? "))
        player_col = int(input(f"Player{symbol.strip()}: Enter column (0, 1, 2)? "))

        # Check if the selected cell is empty
        if board[player_row][player_col] == " 🔮 ":
            board[player_row][player_col] = symbol
        else:
            print("Please choose an empty cell.")
            # Recursively call the function if the cell is not empty
            player_turn(symbol)
    except (ValueError, IndexError):
        print('Invalid Input. Try again.')


# Function to display the current state of the board
def display_board():
    for row in board:
        print("".join(row))


def is_board_full(board):
    return all(board[i][j] != " 🔮 " for i in range(3) for j in range(3))


# Main game loop
game_over = False
while not game_over:
    for symbol in [" ❌ ", " ⭕ "]:
        player_turn(symbol)
        game_over = check_result(symbol)
        print("")
        display_board()
        if game_over:
            print("Game Over.")
            print(f"Player{symbol} wins.")
            game_over = True
            break
        elif is_board_full(board):
            print("Game Over. No one wins.")
            game_over = True
            break


















