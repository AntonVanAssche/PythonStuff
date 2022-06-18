#!/usr/bin/env python3

import random

playerPositions = []
computerPositions = []

playing = True

board = [
   [' ','|',' ', '|', ' '],
   ['-','+','-', '+', '-'],
   [' ','|',' ', '|', ' '],
   ['-','+','-', '+', '-'],
   [' ','|',' ', '|', ' ']
]

def print_board():
   for row in board:
      print(' '.join(row))

def update_board(pos, user):
   if user == 'player':
      symbol = 'X'
   elif user == 'computer':
      symbol = 'O'

   action = {
      1: (0,0),
      2: (0,2),
      3: (0,4),
      4: (2,0),
      5: (2,2),
      6: (2,4),
      7: (4,0),
      8: (4,2),
      9: (4,4)
   }

   action = action[pos]
   board[action[0]][action[1]] = symbol

def check_win():
   if board[0][0] == board[0][2] == board[0][4] == board[0][0] != ' ':
      if board[0][0] == 'X':
         return 'player'
      elif board[0][0] == 'O':
         return 'computer'
   elif board[2][0] == board[2][2] == board[2][4] == board[2][0] != ' ':
      if board[2][0] == 'X':
         return 'player'
      elif board[2][0] == 'O':
         return 'computer'
   elif board[4][0] == board[4][2] == board[4][4] == board[4][0] != ' ':
      if board[4][0] == 'X':
         return 'player'
      elif board[4][0] == 'O':
         return 'computer'
   elif board[0][0] == board[2][0] == board[4][0] == board[0][0] != ' ':
      if board[0][0] == 'X':
         return 'player'
      elif board[0][0] == 'O':
         return 'computer'
   elif board[0][2] == board[2][2] == board[4][2] == board[0][2] != ' ':
      if board[0][2] == 'X':
         return 'player'
      elif board[0][2] == 'O':
         return 'computer'
   elif board[0][4] == board[2][4] == board[4][4] == board[0][4] != ' ':
      if board[0][4] == 'X':
         return 'player'
      elif board[0][4] == 'O':
         return 'computer'
   elif board[0][0] == board[2][2] == board[4][4] == board[0][0] != ' ':
      if board[0][0] == 'X':
         return 'player'
      elif board[0][0] == 'O':
         return 'computer'
   elif board[0][4] == board[2][2] == board[4][0] == board[0][4] != ' ':
      if board[0][4] == 'X':
         return 'player'
      elif board[0][4] == 'O':
         return 'computer'
   else:
      return 'tie'

print('Welcome to Tic Tac Toe!')
print_board()

while playing:
   pos = int(input('Enter a position [1-9]: '))
   while pos not in range(1, 10) or pos in playerPositions or pos in computerPositions:
      print('Invalid position.')
      pos = int(input('Enter a position [1-9]: '))

   playerPositions.append(pos)
   print('You chose position: {}'.format(pos))
   update_board(pos, 'player')

   pos_computer = random.randint(1, 9)
   while pos_computer in playerPositions or pos_computer in computerPositions:
      pos_computer = random.randint(1, 9)

   computerPositions.append(pos_computer)
   print('Computer chose position: {}'.format(pos_computer))
   update_board(pos_computer, 'computer')
   print_board()

   if check_win() == 'player':
      print('You win!')
      playing = False
   elif check_win() == 'computer':
      print('Computer wins!')
      playing = False
