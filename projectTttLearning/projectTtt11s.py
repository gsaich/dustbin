#! /usr/bin/env python
# Tic-Tac-Toe 9 - print board - FTW - add utilities - AI1 - combine checkWin - add strategy
from random import shuffle
from pip._vendor.distlib._backport.shutil import move

board = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
refBoard = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
wins = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ] 
#move = ' '

def play():
    global board
 #   global move
    print('Tic-Tac-Toe')
    print('play against the computer AI level 3')
    printBoards(board)
    while True:
        wipeBoard()
        move = 0
        player_turn = 'X'
        while checkWin(swapPlayer(player_turn)) == False and canMove() == True:
            if player_turn == 'X':
                getMove(player_turn)
                move +=1
            else:
                generateMove()
            printBoards(board)
            player_turn = swapPlayer(player_turn)
        if checkWin(swapPlayer(player_turn)):
            print('Player ', swapPlayer(player_turn), ' wins . . . New Game')
        else:
            print('A draw. . . . New game')
        wipeBoard()
        printBoards(refBoard)
        printBoards(board)


def generateMove():
  #  global move
    corners = [0,2,6,8]
    opposite = [8,6,2,0]
    side = [1,3,5,7]
    adjacent = [0,6,2,8]
    if move == 1:
        moved = False
        for square in range(0,4):
            if board[corners[square]]  == 'X':
                moved = prefMove([opposite[square]])
        for square in range(0,4):
            if board[side[square]]  == 'X':
                moved = prefMove([adjacent[square]])
        if not moved:
            prefMove([0,2,6,8]) # corners
    else:  
        if win_block():
            pass
        elif prefMove([0,2,6,8]): # corners 
            pass
        elif prefMove([4]): # middle
            pass
        else:
            prefMove([1,3,5,7]) # middle row

def prefMove(moves):
    global board
    global move
    moved = False
    move = list()
    for potential in moves:
        if board[potential] == ' ':
            move.append(potential)
    if len(move) !=0:
        shuffle(move)
        board[move[0]] = 'O'
        print('My preferred move is ', move[0] +1)
        moved = True
    return moved
    

def win_block(): # move to win or block
    global board
    testBoard = board
    players = ['O', 'X']
    moveMade = False
    for moveTry in players:
        for square in range(0, len(board)):
            # print('board:     ', board)
            # print('testBoard: ', testBoard)
            if testBoard[square] == ' ' and moveMade == False:
                testBoard[square] = moveTry
                if checkWin(moveTry):
                    board[square] = 'O'
                    moveMade = True
                    print('My move to win or block is ', square + 1)
                else: 
                    testBoard[square] = ' ' # retract move
    return moveMade

def swapPlayer(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

def getMove(player):
    global board
    correct_number = False
    while correct_number == False:
        square = input('Square to place the ' + player + ' ')
        if square == 'q':
            print('You quit.')
            quit()
        try:
            square = int(square)
        except:
            square = -2
        square -= 1 # make input number match internal numbers
        if square >= 0 and square < 9: # number in range - modified from book '10' threw and exception
            if board[square] == ' ': # if it is blank
                board[square] = player
                correct_number = True
            else: 
                print('Square already occupied')
        else:
            print('Incorrect square, try again')


def checkWin(player):
    win = False
    for test in wins:
        count = 0
        for squares in test:
            if board[squares] == player:
                count +=1
        if count == 3:
            win = True
    return win

#def printBoard():
#    print()
#    print('|', end=''),
#    for square in range(0,9):
#        print(board[square],'|', end=''),
#        if square == 2 or square == 5 :
#            print()
#            print('----------')
#            print('|',end=''),
#    print()
#    print()

#def printRefBoard():
#    print()
#    print('|', end=''),
#    for square in range(0,9):
#        print(refBoard[square],'|', end=''),
#        if square == 2 or square == 5 :
#            print()
#            print('----------')
#            print('|',end=''),
#    print()
#    print()

def printBoards(whichBoard):
    print()
    print('|', end=''),
    for square in range(0,9):
        print(whichBoard[square],'|', end=''),
        if square == 2 or square == 5 :
            print()
            print('----------')
            print('|',end=''),
    print()
    print()



def wipeBoard():
    global board
    for square in range(0, len(board)):
        board[square] = ' '

def canMove(): #see is a move can be made
    move = False
    for square in range(0, len(board)):
        if board[square] == ' ':
            move = True
    return move

def somethingsHappeningHere():
    print('. . . what it is aint exactly clear.')

# Here is where everything gets run  !!!!!!!!!!!

#if checkWin ('X'):
#    print('Game Over, X wins!')

#if checkWin ('O'):
#    print('Game Over, O wins!')

print('Here we go  . .  .')
play()