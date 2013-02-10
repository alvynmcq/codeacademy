import random

#loop to create 5 by 5 board consisting of O's.
board = []
for i in range(0,5):
    board.append(["O"]*5)

#function to print board to screen
def print_board(board):
    for row in board:
        print " ".join(row)

#functions to create a random location on the board to hide a battleship
#generates a random row
def random_row(board):
    ship_row = random.randint(0,len(board) - 1)
    return ship_row

#generates a random column   
def random_col(board):
    ship_col = random.randint(0,len(board[0]) - 1)
    return ship_col

#use functions to generate random space on board for battleship
ship_col = random_col(board)
ship_row = random_row(board)

#add for loop that give the player 4 turns to find the battleship
for turn in range(4):
#variables to store users guess
	guess_row = input("Guess Row:")
	guess_col = input("Guess Col:")

#conditions for sinking or missing battleship
	if guess_col == ship_col and guess_row == ship_row:
	    print "Contgratulations! You have sank my battleship!"
	    break
	else:
		if guess_col not in range(0,len(board)) or guess_row not in range(0,len(board)):
			print "Oops, that's not even in the ocean."
		elif board[guess_row] [guess_col] == "X":
				print "You guessed that one already."
		else:
			print "You missed my Battleship!"
			board[guess_row][guess_col] = "X"
	print "You have", (4 - (turn+1)), "turns left"
	print_board(board)

#if statement to check if user is out of guesses, if so "Game Over!"
if turn == 3:
	print "Game Over"