# Requirements
This program is a Tic-Tac-Toe game than can run directly in the IDE without importing anything that isn't built-in. It first
prints the instructions for the user. Then it randomly chooses  player 1 or 2 to go first. They will be asked to make a move
on an ASCII board by entering a number from 1 to 9, with each number corresponding to one space. It then prints the board, 
with the desired move showing. The user is told if their move is invalid for any reason. They can also type "hint" to get a 
hint from the computer or "?" to see the instructions. Then the turn passes to the next player. This process repeats until the 
board is full or until one player has won by getting three in a row. The players are asked if they would like to replay the 
game. Typing anything starting with "y" should replay the game. Typing anything else will not.

# Design
First, there's a class called TicTacToe that contains all the main functions. It has functions that draw the board, pick
someone to go first, make moves, get hints, define a temporary duplicate of the board, check if a space is vacant, process 
player moves, and check if the board is full (tie). TicTacToe also has a representation function if the user wants to print 
its object. First an object called game is created using the TicTacToe class. First, the program will print instructions for 
the user using the instructions function that is in the TicTacToe class. Next a while loop is used to let the game be replayed 
as many times as the user wants. If the user wants to stop playing, then the program breaks the loop. The whoGoesFirst() 
function randomly selects a player to go first. The turn value is set to the output of that function. Then, for each 
game, the program will do the following:

1. Print the board using an ASCII representation.
2. Use getPlayerMove() to interpret the move that player wanted to make.
3. Use makeMove() to actually represent and register that move.
4. Check if that player won or tied, in which case skip step 5.
5. Pass the turn to the other player and return to step 1.
6. End the game. If the user wants to replay, then reset the board and go back to step 1. If not, break the loop.

If the player wants to see the instructions, they can type "?" to call the printInstructions() function. It simply prints the 
instructions. If they type "hint" instead of making a move, then the function getHint() is called. It in turn uses a series of
other functions inside the TicTacToe class, which allows the computer to determine the best move, or one of the best moves. 
How it works is described in the code comments in the program. Finally, the end of the program uses the playAgain() function 
to ask the user if they'd like to play again. If they do, then it returns True, which allows the loop to restart, which in 
effect restarts the game. If they don't, however, the function returns False, which causes the loop to terminate, ending the 
program.
