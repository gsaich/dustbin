#! /usr/bin/env python
# Tic-Tac-Toe 9 - print board - FTW - add utilities - AI1 - combine checkWin - add strategy
from random import shuffle

board = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
refBoard = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
# board = [ 'O', 'X', ' ', 'O', ' ', 'X', 'O', 'X', 'X' ]
wins = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ] 

def play():
    global board
    print('Tic-Tac-Toe')
    print('play against the computer AI level 1+')
#    printBoards(board)