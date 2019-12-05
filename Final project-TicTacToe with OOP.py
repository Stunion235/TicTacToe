#Tic Tac Toe
#Note: I worked alone for this project. I already put it in Github:
#https://www.github.com/Stunion235/TicTacToe

#ADDED USER-FRIENDLY IMPROVEMENTS:
# 1. Defined a getHint() function that is called if the user types 'hint' for a move.
# 2. Implemented a __repr__() for the TicTacToe class if the user wants to print it.
# 3. Prints instructions and can tell the user is a move is not valid.

import random

class TicTacToe():
    def __repr__(self):
        return('<\nClass Name: ' + self.__class__.__name__ + '\nCurrent Turn: Player ' + str(turn) + '\nBest Move: ' + str(self.getHint()) + '\nTied: ' + str(self.isBoardFull(theBoard)) + '\nGame over: ' + str(not(gameIsPlaying)) + '\n>')
    def drawBoard(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        return(random.randint(1,2))

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            print('Player', turn, 'what is your move?', end='\t')
            move = input()
            #Check if the move is a number, 'hint', or '?'. If not, the user is told so.
            if move.upper() not in '1 2 3 4 5 6 7 8 9 HINT ?'.split():
                print('Invalid move. Enter a number from 1 to 9 or type hint for a hint.')
                move = '0'
            #Check if the space is free. If not, the user will be alerted. 
            elif move.isnumeric() and not(self.isSpaceFree(board, int(move))):
                print('That space is occupied.')
                move = '0'
            #Do the appropriate task if the user typed "hint" or "?".
            elif move.lower() == 'hint':
                print('Hint:', self.getHint(), '\n')
            elif move == '?':
                self.printInstructions()
        return int(move)

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self, board, Letter2):
        # Given a board and the computer's letter, determine where to move and return that move.
        if Letter2 == 'X':
            Letter1 = 'O'
        else:
            Letter1 = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, Letter2, i)
                if self.isWinner(copy, Letter2):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, Letter1, i)
                if self.isWinner(copy, Letter1):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if (move != None):
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True

    #Uses the getComputerMove() function to provide the player with a hint.
    def getHint(self):
        return(game.getComputerMove(theBoard, '0'))

    #Print the instructions if user types "?" for a move.
    def printInstructions(self):
        print('='*23)
        print('Instructions:')
        print('When you are asked for a move, enter a number from 1-9 and press enter.')
        print('They correspond to the spaces in the same way as the keys on a numeric keypad:\n')
        print('7 8 9')
        print('4 5 6')
        print('1 2 3')
        print('\nYou can also type "hint" for a hint or "?" to see these instructions.')    
        print('='*78)

#Define the object game to be of the class TicTacToe.     
game = TicTacToe()
print('\nWelcome to Tic Tac Toe!'.upper())
game.printInstructions()
while True:
    #Reset the board
    theBoard = [' '] * 10
    Letter1, Letter2 = ['X', 'O']
    turn = game.whoGoesFirst()
    print('Player', turn, 'will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 1:
            #Player 1's turn.
            print('It is Player 1\'s turn.')
            game.drawBoard(theBoard)
            move = game.getPlayerMove(theBoard)
            game.makeMove(theBoard, Letter1, move)
            print()
            #Check if Player 1 won or for a tie.
            if game.isWinner(theBoard, Letter1):
                game.drawBoard(theBoard)
                print('Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
            turn = 2

        else:
            #Player 2's turn.
            print('It is Player 2\'s turn.')
            game.drawBoard(theBoard)
            move = game.getPlayerMove(theBoard)
            game.makeMove(theBoard, Letter2, move)
            print()
            #Check if Player 2 won or for a tie.
            if game.isWinner(theBoard, Letter2):
                game.drawBoard(theBoard)
                print('Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
            turn = 1

    if not game.playAgain():
        break
