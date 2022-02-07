#  Final Project: Even Colourful Game
#  Developer: Derek Jungmin Shin and David Choi
#  Date: 11/28/2020
import cmpt120imageWeek9

def welcome():
	# Prints the beginning messages
	print("")
	print("Dear player! Welcome to the Even Colorful game")
	print("================================================")
	print("")
	print("With this system you will be able to play as many games as you want!")
	print("The objective of this game is that all columns and rows in the board")
	print("add to an even number.")
	print("For each game:")
	print("- you will be able to choose to play 'solo' or against the computer ('AI'),")
	print("- you will be able to choose an initial board,")
	print("- at the end of each game you will win (or lose) points, and")
	print("- you will see a colorful representation of the game final board results.")
	print("Enjoy!")
	print("")


# This function returns the largest number in a list
def find_max(lst):
	'''
	Input parameter:
		lst - an array that contains the total sum of each row and column
	Returns:
		biggest - the largest integer in the given array
	'''
	# Assigns the first number of the list as the largest number 
	biggest = lst[0]
	
	# Goes through the list and updates the largest number of the list
	# Appropriately after every iteration
	for i in range(len(lst)):
		if lst[i] > biggest:
			biggest = lst[i]
	# Returns the largest number of the list
	return biggest


def listOfCol(board_data, sumOfCol):
	'''
	Input parameter:
		board_data - 2D array of the current board data
		sumOfCol - the list that will contain the sum of columns
	Returns:
		sumOfCol - the list that contains the sum of columns
	'''
	# Initialize the column number
	col = 0
	# Repeat the loop until it goes through every index
	for allCol in range(len(board_data)):
		# Add the total of the lists with the same index
		# and add it to the final list
		for oneCol in range(len(board_data)):
			col = col + int(board_data[oneCol][allCol])
		sumOfCol.append(col)
		# Reset the variable
		col = 0
	return sumOfCol


def listOfRow(board_data, sumOfRow):
	'''
	Input parameter:
		board_data - 2D array of the current board data
		sumOfRow - the list that will contain the sum of rows
	Returns:
		sumOfRow - the list that contains the sum of rows
	'''	
	# Initialize the row number
	row = 0
	# Repeat loop until it goes through every list
	for allRow in range(len(board_data)):
		# Add the total of each list 
		# and add it to the final list
		for oneRow in range(len(board_data)):
			row = row + int(board_data[allRow][oneRow])
		sumOfRow.append(row)
		# Reset the variable
		row = 0
	return sumOfRow


def listRowImage(col, length):
	"""
	Input parameter: 
		col - list of the sum of columns
		length - length of pixels in the square
	Returns: 2D array with the rgb values to print the vertical image
	"""

	# Open the file with the colours and get rid of the first line
	colour = open("colorcoding.csv")
	colour.readline()

	# Create a list combining all the colours
	list1 = []
	for number in colour:
		list1.append(number.strip().split(",")[1:])

	# Create the black lines separating the colours
	black = [0, 0, 0]
	black1D = []
	# Make the length 10 pixels long because
	# the image is vertical
	for i in range(10):
		black1D.append(black)

	# Create an initial list that will contain all the rgb values
	finalImage = []
	# Create the rgb 2D array with all the colours
	for i in range(len(col)):
		colourNum = col[i]
		rgbVal = []
		# Get the rgb values to make the first colour
		for i in range(len(list1[colourNum])):
			rgbVal.append(int(list1[colourNum][i]))
		rgb2 = []
		# Add the rgb values to get the length
		for i in range(length):
			rgb2.append(rgbVal)
		# Add the black lines inbetween the colours
		finalImage = finalImage + rgb2 + black1D

	# Add the list with the rgb values to get the width
	finalImage1 = []
	for i in range(length):
		finalImage1.append(finalImage)
	return finalImage1


def listColImage(line, length):
	"""
	Input parameter: 
		line - list of the sum of rows
		length - length of pixels in the square
	Returns: 2D array with the rgb values to print the horizontal image
	"""

	# Open the file with the colours and get rid of the first line
	colour = open("colorcoding.csv")
	colour.readline()

	# Create a list combining all the colours
	list1 = []
	for number in colour:
		list1.append(number.strip().split(",")[1:])

	# Create the black lines separating the colours
	black = [0, 0, 0]
	black1D = []
	# Make the the pixels length long
	for i in range(length):
		black1D.append(black)
	black2D = []
	# Make the pixels 10 wide
	for i in range(10):
		black2D.append(black1D)

	# Create an initial list that will contain all the rgb values
	finalImage = []
	# Create the rgb 2D array with all the colours
	for i in range(len(line)):
		colourNum = line[i]
		rgbVal = []
		# Get the rgb values to make the first colour
		for i in range(len(list1[colourNum])):
			rgbVal.append(int(list1[colourNum][i]))
		# Add the rgb values to get the length
		rgb2 = []
		for i in range(length):
			rgb2.append(rgbVal)
		# Add the rgb values to get the width
		rgb3 = []
		for i in range(length):
			rgb3.append(rgb2)
		# Add the colours with the black divider inbetween
		finalImage = finalImage + rgb3 + black2D
	return finalImage


def printBoard(array2D):
	'''
	Input parameter:
		array2D - an array with the numbers for the board
	Returns: prints a board depending on the 2D array
	'''
	# Printing spaces for the board
	print("       ", end = "")
	# Prints the first line with the column
	for x in range(len(array2D[0])):
		print("   Col ", x, end = "")
	print("\n")
	# Prints the rows 
	for i in range(len(array2D[0])):
		print("Row ", i, end = " ")
		# Prints the number in the rows
		for y in range(len(array2D[0])):
			print("      ",array2D[i][y], end = "")
		print("\n")


def create_initial_board(boardID):
	'''
	Input parameter: 
		boardID - the board number
	Returns: prints the inital board and returns 
			 the list of the board
	'''
	# Open the board file depending on the user's input
	if boardID == "1":
		board = open("board1.csv")
		# Get the number in the first line representing the 
		# number of rows and columns
		boardtest = board.readline().strip().replace(',', '')
	elif boardID == "2":
		board = open("board2.csv")
		# Get the number in the first line representing the 
		# number of rows and columns
		boardtest = board.readline().strip().replace(',', '')
	elif boardID == "3":
		board = open("board3.csv")
		# Get the number in the first line representing the 
		# number of rows and columns
		boardtest = board.readline().strip().replace(',', '')
		
	board_data = []
	# Get all the numbers of the board into a list of a list
	for i in range(int(boardtest)):
		line = board.readline().strip("\n").split(",")
		board_data.append(line)

	# Printing spaces for the board
	print("       ", end = "")
	# Prints the first line with the column
	for x in range(len(board_data[0])):
		print("   Col ", x, end = "")
	print("\n")
	# Prints the rows 
	for i in range(len(board_data[0])):
		print("Row ", i, end = " ")
		# Prints the number in the rows
		for y in range(len(board_data[0])):
			print("      ",board_data[i][y], end = "")
		print("\n")
	return board_data

    
