# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

board = '  | |  -----  | |  -----  | | '

status = 'playing'

switcher = {
  1: 1,  2: 3,  3: 5,
  4: 13, 5: 15, 6: 17,
  7: 25, 8: 27, 9: 29
}

def play_game(board, starting_player):
  player = starting_player
  render_board(board)
  i = 0
  while status == 'playing':
    choice = int(input('Enter a number between 1-9: '))
    move = switcher.get(choice, 'Invalid Move')
    if board[move] == ' ':
      board = board[:move] + player + board[move+1:]
      render_board(board)
      if player == 'x': player = 'y'
      else: player = 'x'
      i += 1
      if i >= 2: evaluate_game(board, player, i)
    else:
      print('That move has already been played')
  else:
    render_board(board)
    return status

def render_board(board):
  for item in [board[i:i+6] for i in range(0, len(board), 6)]:
    print(item)

def evaluate_game(board, player, i):
  global status
  # horizontal across
  if board[1] == player and board[3] == player and board[5] == player:
    print('h1', board[1], board[3], board[5], player)
    status = player + ' wins!'
  elif board[13] == player and board[15] == player and board[17] == player:
    print('h2')
    status = player + ' wins!'
  elif board[25] == player and board[27] == player and board[29] == player:
    print('h3')
    status = player + ' wins!'
  # vertical across
  elif board[1] == player and board[13] == player and board[25] == player:
    print('v1')
    status = player + ' wins!'
  elif board[3] == player and board[15] == player and board[27] == player:
    print('v2')
    status = player + ' wins!'
  elif board[5] == player and board[17] == player and board[29] == player:
    print('v3')
    status = player + ' wins!'
  # diagonal
  elif board[1] == player and board[15] == player and board[29] == player:
    print('d1')
    status = player + ' wins!'
  elif board[5] == player and board[15] == player and board[25] == player:
    print('d2')
    status = player + ' wins!'
  # tie
  elif status == 'playing' and i == 9: status = 'Tied game!'
  print(i)

play_game(board, 'x')
