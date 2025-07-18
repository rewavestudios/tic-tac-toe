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
