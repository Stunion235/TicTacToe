# Requirements
This program is a Tic-Tac-Toe game than can run directly in the IDE without importing anything that isn't built-in. It first
prints the instructions for the user. Then it randomly chooses  player 1 or 2 to go first. They will be asked to make a move
on an ASCII board by entering a number from 1 to 9, with each number corresponding to one space. It then prints the board, 
with the desired move showing. The user is told if their move is invalid for any reason. They can also type "hint" to get a 
hint from the computer or "?" to see the instructions. Then the turn passes to the next player. This process repeats until the 
board is full or until one player has won by getting three in a row. The players are asked if they would like to replay the 
game. Typing anything starting with "y" should replay the game. Typing anything else will not.

# Design
First I have a class called TicTacToe that contains all the main functions. The class has functions that draw the board, pick someone to go first, make moves, get hints, define a temporary duplicate of the board, check if a space is vacant, process player moves, and check if the board is full (tie). First an object called game is created using the TicTacToe class.
