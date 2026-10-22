import random

def print_board(board):
  for row in board:
    for cell in row:
      if cell == 0:
        print(" ", end=" ")
      elif cell == 1:
        print("X", end=" ")
      elif cell == -1:
        print("O", end=" ")
    print()

def check_win(board, player):
  win_conditions = [
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    [board[0][0], board[1][1], board[2][2]],
    [board[2][0], board[1][1], board[0][2]],
  ]
  for condition in win_conditions:
    if all(cell == player for cell in condition):
      return True
  return False

def check_draw(board):
  for row in board:
    for cell in row:
      if cell == 0:
        return False
  return True

def player_move(board):
  while True:
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == 0:
      return row, col
    else:
      print("Invalid move. Try again.")

def computer_move(board):
  empty_cells = []
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        empty_cells.append((i, j))
  row, col = random.choice(empty_cells)
  return row, col

def main():
  board = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
  turn = 1  # 1 for player, -1 for computer
  while True:
    print_board(board)
    if turn == 1:
      row, col = player_move(board)
      board[row][col] = 1
    else:
      row, col = computer_move(board)
      board[row][col] = -1
    if check_win(board, turn):
      print_board(board)
      if turn == 1:
        print("Player wins!")
      else:
        print("Computer wins!")
      break
    elif check_draw(board):
      print_board(board)
      print("It's a draw!")
      break
    turn *= -1

if __name__ == "__main__":
  main()