from termcolor import colored   # For coloring player symbols (X/O) in terminal output

# Define player symbols
X = 'X'
O = 'O'

# Initialize 3x3 board with empty spaces
board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

# Color the cell mark based on player
def cell(mark):
  color = 'red' if mark == X else 'green'   # X is red, O is green
  return colored(mark, color)

# Render the current board state with row separators
def print_board(board):
  line = '---+---+---'
  print(line)
  for row in board:
    # Print each row with colored cells and vertical separators
    print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])}')
    print(line)

# Evaluate board state for any win condition  
def check_winner(board):
  # Row check: if all 3 cells in a row are the same and not empty
  for row in board:
    if row[0] == row[1] == row[2] != ' ':
      return True

  # Column check: iterate 0–2 and check top-to-bottom values
  for column in range(3):
    if board[0][column] == board[1][column] == board[2][column] != ' ':
      return True

  # Diagonal checks (both directions)
  if board[0][0] == board[1][1] == board[2][2] != ' ' or \
     board[0][2] == board[1][1] == board[2][0] != ' ':
     return True

  return False    # No win condition met

# Utility to check if the board is full (used to detect a draw)
def is_full(board):
  for row in board:
    if ' ' in row:
      return False
  return True
