# Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.

def eightQ():
  
  def isValid(board):
    for i in range(8):
      # horizontal
      if sum(board[i]) > 1:
        return False
      # vertical
      if sum([ row[i] for row in board ]) > 1:
        return False
    # diagonal
    for i in range(-8, 8):
      if sum([ board[k][k + i] for k in range(8) if 0 <= k + i <= 7 ]) > 1:
        return False
    for i in range(16):
      if sum([ board[k][i - k] for k in range(8) if 0 <= i - k <= 7 ]) > 1:
        return False
    return True
  
  import copy
  def _eightQ(board, row):
    if row == 8:
      total[0] += 1
      answers.append(board)
    else:
      for col in range(8):
        b = copy.deepcopy(board)
        b[row][col] = 1
        if isValid(b):
          _eightQ(b, row + 1)
  
  total = [0]
  answers = []
  board = [ [0] * 8 for _ in range(8) ]
  _eightQ(board, 0)
  return total[0], answers