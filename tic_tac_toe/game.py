import math
import re

class Board():
  SCORES = { 'tie': 0, 'X': 10, 'O': -10 }

  def __init__(self):
    self.state = self.__initialize_board()

  #
  # DESC:
  # Displays the grid to view the current state of the board
  #
  def display(self):
    cell = 0
    print("---------------")
    for row in self.state:
      for column in row:
        cell += 1
        if len(column) == 0:
          element = str(cell )
        else:
          element = column
        print('| %s |'%(element), end='')
      print("\n---------------")

  #
  # DESC:
  # Returns the list of empty cells
  #
  def empty_cells(self):
    cells = []
    for row in range(3):
      for column in range(3):
        if self.state[row][column] == '':
          cells.append([row, column])
    return cells

  #
  # DESC:
  # Returns the integer score given a value like `tie`, `X`, or `O`
  #
  def get_score(self, status):
    return Board.SCORES[status]

  #
  # DESC:
  # A set of terminal conditions where the game stops.
  # 1. returns `tie`: when no more moves left / open positions left
  # 2. returns `winner (X/O)`: when either horizontal, vertical or diagonal elements match
  #
  def isCompleted(self):
    winner = None

    # Horizontal: when elements are same
    for row in range(3):
      if self.state[row][0] != '' and self.state[row][0] == self.state[row][1] and self.state[row][1] == self.state[row][2]:
        winner = self.state[row][0]

    # Vertical: when elements are same
    for column in range(3):
      if self.state[0][column] != '' and self.state[0][column] == self.state[1][column] and self.state[1][column] == self.state[2][column]:
        winner = self.state[0][column]

    # Diagonal (top-left to bottom-right): when elements are same
    if self.state[0][0] != '' and self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]:
      winner = self.state[0][0]

    # Diagonal (top-right to bottom-left): when elements are same
    if self.state[0][2] != '' and self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]:
      winner = self.state[0][2]

    # open position left
    open_positions = 0
    open_positions = len(self.empty_cells())

    # `tie` when no moves left as well as no winner is set
    # else, winner is set
    if open_positions == 0 and winner == None:
      return 'tie'
    else:
      return winner

  #
  # DESC:
  # Maps integer position to row and column within the board provided by a player
  #
  # ARGS:
  # @position is an integer
  #
  def map_to_cell(self, position):
    _position = position - 1
    row = _position//3
    column = _position%3
    return [row, column]

  #
  # DESC:
  # Maps integer position to row and column within the board provided by a player
  #
  def start(self):
    self.display()

  #
  # DESC:
  # Ensures if a move made is valid
  # i.e. should be blank and integer within the range of the length of the matrix. Here it is 3x3 matrix
  #
  # ARGS:
  # `position` is the user's input and is a string
  #
  def is_valid_move(self, position):
    # 1. Ensure string has only single positive digit
    move = re.match('^\d$', position)
    if move == None:
      return False

    # 2. Position is between 1-9
    _position = int(position)
    if not (_position >=1 and _position <= 9):
      return False

    # 3. Check if the position is available for the move
    row, column = self.map_to_cell(_position)
    if self.state[row][column] != '':
      return False

    return True

  def __initialize_board(self):
    return [
      ['', '', ''],
      ['', '', ''],
      ['', '', '']
    ]


class Player():
  QUALIFIED_IDENTIFIERS = ['X', 'O']

  def __init__(self, name):
    self.name = name
    self.identifier = None

  #
  # DESC:
  # Each player type will implement its own move whether it is interactive, random, or calculative
  # a. interactive in case of human player
  # b. calculative in case of computer-controlled player
  # c. random in case of computer-controlled player but not calculative
  #
  # ARGS:
  # @board is the board object
  #
  def best_move(self, board):
    raise Exception("Implementation error")

  #
  # DESC:
  # Present interactive commands/prompts to the players
  #
  def prompt(self):
    raise Exception('Implementation error')


# DESC:
# HumanPlayer asks for the position of a cell on the board for its move
#
class HumanPlayer(Player):
  def __init__(self, name):
    super().__init__(name)
    self.identifier = 'O'

  #
  # DESC:
  # When human is playing, prompts the position to be filled in
  # In case of the cell already filled in, player is asked to fill in the correct cell
  #
  def best_move(self, board):
    while True:
      self.prompt()

      position = input("Enter position 1-9: ")
      if board.is_valid_move(position) == True:
        break
    row, column = board.map_to_cell(int(position))
    board.state[row][column] = self.identifier

  #
  # DESC:
  # Present interactive commands/prompts to the players
  #
  def prompt(self):
    print('\n%s\'s turn...'%(self.name))


# DESC:
# This is computer-simulated player where each move is calculated to be optimal.
# To calculate optimal move, this uses minimax algorithm.
#
# Given a board and its state, minimax algorithm considers all the next possible moves
#  and evaluates the moves to minimize the possible loss for a worst case
#
class ComputerPlayer(Player):
  def __init__(self, name):
    super().__init__(name)
    self.identifier = 'X'

  #
  # DESC:
  # Evaluates the possible move by considering the moves of the other player and minimizing its gain, thus, maximizing its chance to winning
  #
  def best_move(self, board):
    self.prompt()

    current_board = board.state
    # 1. Set to the lowest score possible
    best_score = -math.inf
    # 2. Initialize empty move
    move = []
    # 3. Start iterating over each cell to calculate the scores
    for row in range(3):
      for column in range(3):
        # 3.1 Determine the move on an empty cell
        if(current_board[row][column] == ''):
          # 3.2 Consider if the current cell is the possible move temporarily
          current_board[row][column] = 'X'
          # 3.3 Play the other player's turn to understand the possible gains till we reach the terminal node
          #     and capture the score from every decision taken when both players play together
          score = self.minimax(board, 0, False)
          # 3.4 As this is an evaluation, empty the current cell
          current_board[row][column] = ''
          # 3.5 If the new score is greater than previous score, then consider it as the best score
          if score > best_score:
            best_score = score
            # 3.6 Set the cell as the optimal move
            move = [row, column]

    # 4. Make the move with the optimal position calculated above
    current_board[move[0]][move[1]] = self.identifier

  #
  # DESC:
  # Minimax iterates over the board recursively that has the moves played by both the players
  # Given a state of the board, a player makes move at empty cells, of which determines how optimal moves other players make
  # This is done recursively until we reach a terminal state where either all the cells are filled in (in case of tie) or
  #   either of the player wins
  #
  # ARGS:
  # @board is the current state of the board when each player assumes the position and calculates the scores
  # @depth notes how deep is the recursion for a decision taken. Just for debugging as of now
  # @isMaximizingPlayer is the conputer-controller player and is `true` whereas it is`false` when trying to predict the outcome of the moves taken
  #
  def minimax(self, board, depth, isMaximixingPlayer):
    # 1. Terminal condition to determine if the its a tie or any player has won and returns the score
    status = board.isCompleted()
    if status != None:
      return board.get_score(status)

    # 2. Set the current state of the board
    current_board = board.state

    # 3. Current and opponent players playing their turns one-by-one
    if isMaximixingPlayer == True:
      # Set to the lowest score possible
      best_score = -math.inf
      for row in range(3):
        for column in range(3):
          # 3.1 Determine the move on an empty cell
          if current_board[row][column] == '':
            # 3.2 Consider if the current cell is the possible move temporarily
            current_board[row][column] = 'X'
            # 3.3 Play the other player's turn to understand the possible gains till we reach the terminal node
            #     and capture the score from every decision taken when both players play together
            score = self.minimax(board, depth+1, False)
            # 3.4 As this is an evaluation, empty the current cell
            current_board[row][column] = ''
            # 3.5 If the new score is greater than previous score, then consider it as the best score
            if score > best_score:
              best_score = score

      # 4. Returns the best score after all the cells in the board are visited
      return best_score
    else:
      # Set to the highest score possible
      best_score = math.inf
      for row in range(3):
        for column in range(3):
          # 3.1 Determine the move on an empty cell
          if current_board[row][column] == '':
            # 3.2 Consider if the current cell is the possible move temporarily with the opponent
            current_board[row][column] = 'O'
            # 3.3 Play the current player's turn to understand the possible gains till we reach the terminal node
            #     and capture the score from every decision taken when both players play together
            score = self.minimax(board, depth+1, True)
            # 3.4 As this is an evaluation, empty the current cell
            current_board[row][column] = ''
            # 3.5 If the new score is greater than previous score, then consider it as the best score
            if score < best_score:
              best_score = score

      # 4. Returns the best score after all the cells in the board are visited
      return best_score

  #
  # DESC:
  # Present interactive commands/prompts to the players
  #
  def prompt(self):
    print('\n%s\'s turn...'%(self.name))

class Game():
  def __init__(self):
    self.players = []
    self.board = Board()
    self.winner = None
    self.status = None
    self.current_player = None

  #
  # DESC:
  # Add a new distinct player not more than 2 in a game
  #
  def add_player(self, player):
    permission = self.__is_allowed_to_add(player)

    if permission == True:
      self.players.append(player)
    else:
      print('Only 2 distinct players allowed')

  #
  # DESC:
  # Announces the winner or tie
  #
  def announce(self):
    if self.status == 'tie':
      print("Ooh! It's a tie.\n\n")
    else:
      self.winner = self.current_player
      print('Game over. %s wins!\n\n'%(self.winner.name))

  #
  # DESC:
  # Game is started with this method that lets users to play turn-by-turn
  # Declare the winner. If not, it's a tie 
  #
  def play(self):
    # 1. Set up the board and start
    print('\nWelcome, %s and %s.'%(computer_player.name, human_name))
    print("Here's your board. Let's start!")
    self.board.start()

    # 2. Start with the first player and set it as the current player
    self.current_player = self.players[0]

    # 3. Players play turn-by-turn
    while True:
      # 3.1 Fetch the best move i.e. best move by computer-controlled player or human input
      self.current_player.best_move(self.board)

      # 3.2 Display the board after the move
      self.board.display()

      # 3.3 Terminal condition to stop the game
      # Either tie or winner
      self.status = self.board.isCompleted()
      if self.status != None:
        break
      else:
        next_player = [item for item in self.players if item.identifier != self.current_player.identifier][0]
        self.current_player = next_player

    # 4. Announce the winner or tie
    self.announce()

  #
  # DESC:
  # Ensure only X and O are permitted
  #
  def __is_allowed_to_add(self, player):
    # 1. Ensure only 2 players are allowed
    if not len(self.players) < 2:
      return False

    # 2. Ensure distinct players are added i.e. X and O
    identifiers = [player.identifier for player in self.players]
    if player.identifier in identifiers:
      return False

    # 3. Ensure only X and O are allowed
    if player.identifier not in Player.QUALIFIED_IDENTIFIERS:
      return False

    # 4. Else, player is allowed
    return True
