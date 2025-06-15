class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def display_board(self):
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print("  -----------")
    
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Players will take turns. Player X goes first.")
        print("Enter row and column numbers (0-2) to make your move.\n")
        
        while True:
            self.display_board()
            print(f"\nPlayer {self.current_player}'s turn")
            
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input! Please enter numbers between 0-2.")
                    continue
                
                if not self.make_move(row, col):
                    print("That position is already taken! Try again.")
                    continue
                
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"\n🎉 Player {winner} wins! 🎉")
                    break
                
                if self.is_board_full():
                    self.display_board()
                    print("\n🤝 It's a tie! 🤝")
                    break
                
                self.switch_player()
                
            except ValueError:
                print("Invalid input! Please enter numbers only.")
            except KeyboardInterrupt:
                print("\nGame interrupted. Thanks for playing!")
                break

# To run the game:
# game = TicTacToe()
# game.play()

print("="*60)
print("SAMPLE OUTPUT - Complete Game Demonstration")
print("="*60)

# Simulate a complete game
sample_game = TicTacToe()

print("Welcome to Tic Tac Toe!")
print("Players will take turns. Player X goes first.")
print("Enter row and column numbers (0-2) to make your move.\n")

# Sample game moves that lead to X winning
game_moves = [
    (1, 1, "X"),  # X takes center
    (0, 0, "O"),  # O takes top-left
    (0, 1, "X"),  # X takes top-middle
    (2, 2, "O"),  # O takes bottom-right
    (2, 1, "X"),  # X takes bottom-middle and wins!
]

for i, (row, col, player) in enumerate(game_moves):
    # Show current board state
    print(f"\n   0   1   2")
    for r in range(3):
        print(f"{r}  {sample_game.board[r][0]} | {sample_game.board[r][1]} | {sample_game.board[r][2]}")
        if r < 2:
            print("  -----------")
    
    print(f"\nPlayer {sample_game.current_player}'s turn")
    print(f"Enter row (0-2): {row}")
    print(f"Enter column (0-2): {col}")
    
    # Make the move
    sample_game.make_move(row, col)
    
    # Check for winner after move
    winner = sample_game.check_winner()
    if winner:
        # Show final board
        print(f"\n   0   1   2")
        for r in range(3):
            print(f"{r}  {sample_game.board[r][0]} | {sample_game.board[r][1]} | {sample_game.board[r][2]}")
            if r < 2:
                print("  -----------")
        print(f"\n🎉 Player {winner} wins! 🎉")
        break
    
    # Switch to next player
    sample_game.switch_player()

print("\n" + "="*60)
print("SAMPLE OUTPUT - Error Handling")
print("="*60)

print("\nExample of invalid input handling:")
print("Player X's turn")
print("Enter row (0-2): 5")
print("Enter column (0-2): 1")
print("Invalid input! Please enter numbers between 0-2.")
print("\nPlayer X's turn")
print("Enter row (0-2): 1")
print("Enter column (0-2): 1")
print("That position is already taken! Try again.")

print("\n" + "="*60)
print("GAME FEATURES:")
print("• 3x3 grid with coordinate system (0-2)")
print("• Two players take turns (X and O)")
print("• Input validation for coordinates")
print("• Detects wins (rows, columns, diagonals)")
print("• Detects tie games")
print("• Clear board display")
print("• Error handling for invalid moves")
print("="*60)