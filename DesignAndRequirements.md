# Requirements
The purpose of this program is to simulate a two-player Tic-Tac-Toe game. The objective of Tic-Tac-Toe is for each player to take turns placing X's or O's on a 3 by 3 board with the aim of getting three of their symbol in a row, column, or diagonal, while preventing the other player from doing so. The first player to achieve this is the winner. If no player can do this, there is a tie.

The game should provide instructions for the user so they can play and navigate the game. Then it should randomly choose player 1 or 2 to go first. The player should then be able to make a move on an ASCII board by entering a number from 1 to 9, with each number corresponding to one space in the virtual 3 by 3 board. The mapping of numbers to spaces needs to be the same as the arrangement of numbers on a numeric keypad. Before each turn, the program should print the board's current state, with all the past moves represented as an X or an O character in their respective "spaces". If the user makes an invalid move, then the program should let them know. That should happen if the desired space is already occupied by a symbol, or if they did not type a number from 1 to 9. Users should also be able to type "hint" to get a hint from the computer or "?" to see the instructions. Then the turn should pass to the next player, as with a normal game of Tic-Tac-Toe. Players should be able to play in this manner until the board is full, which is a tie, or until one player has won by getting three in a row. Then, the players should get to choose if they would like to play a new game by typing anything starting with "y". If anything else is typed, then the game should end.

# Design
The class called TicTacToe implements the game and its operation. The board itself is represented and interpreted within the class and its functions as a list of strings. The class has functions to do the following:
1. *drawBoard(board)*, which prints the board. It will be called before each turn.
2. *whoGoesFirst()*, which picks someone to go first. It is run once at the beginning of each game.
3. *makeMove(board, letter, move)*, which is used to represent the players' moves by putting their move into the board data if it is valid.
4. *getHint()*, which is simply used to give the player hints.
5. *getBoardCopy(board)*, which defines a temporary duplicate of the board. The reason for this is to let the AI "think" without affecting the board that the players see.
6. *isSpaceFree(board, move)*, which is used to check if a desired space is vacant on the board. It returns one Boolean value, True if the space is free and False otherwise. 
7. *getPlayerMove(board)*, which processes player moves.
8. *isBoardFull(board)*, which will check if the board is full. Such a full board constitutes a tie.
9. *isWinner(board, letter)*, which checks if a given move will result in a victory for either player.
10. *\_\_repr()\_\_*, which is a system function for any classes that lets its object be printed readably.

**Structure of the main program**
 * Create an object called game, of the TicTacToe class. 
 * Print the instructions for the players using the *printInstructions()* class function. 
 * As long as players want to play the game:
    1. Pick someone to make the first move using *whoGoesFirst()*.
    2. Print the ASCII representation of the board using *drawBoard()*.
    3. Ask for and interpret the player's move using *getPlayerMove()*.
    4. Represent and register that move using *makeMove()*.
    5. Check if that player won or tied using *isWinner()* and *isBoardFull()* respectively, in which case skip step 6.
    6. Pass the turn to the other player and return to step 1, starting a new turn.
 * End the game. If the players want to replay, then reset the board and go back to step 1. If not, break the loop.

**Design notes:**
 * During *getPlayerMove()*, if the player types "?", the *printInstructions()* function is called to show the instructions. Likewise, if they type "hint" instead of making a move, then the function *getHint()* is called to provide a hint. *getHint()* in turn uses a series of other functions inside the TicTacToe class, which allows the computer to determine the best move, or one of the best moves. The algorithm used in *getHint()* is described in the code comments in the program. 
 * The end of the program uses the *playAgain()* function to ask the players if they'd like to play again. If they do, then it returns True, which allows the loop to reiterate, which in effect restarts the game. If they don't, however, the function returns False, which causes the loop to terminate, ending the program.
