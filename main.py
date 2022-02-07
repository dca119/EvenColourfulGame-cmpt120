# Even Colourful Game
# Authors: Derek Jungmin Shin and David Choi
# Date: 11/28/2020
# This program creates a simulation of the even colorful game

# Imports
import cmpt120imageWeek9
import createBoardImages
import random
import time

# Default message to the user for the purpose of explaining the rules
createBoardImages.welcome()

# Asks the user if they want to run the program
playing_response = input("Would you like to play? (y/n): ").lower()
print("")

# Initialize points tally for the user, computer, and the total score achieved
total_score = 0
user_score = 0
computer_score = 0
# One time default variables
playing = True
# The tally for the game number which increases everytime a new game is played
game_num = 1
# The default value of the boolean that tells the progrma not to output
# The total score of the games when no games have been played
first_time_bye_prompt = True
# The program will continue to play new games until the user 
# Ends the program through a prompt repeating every iteration of the game
while 'y' == playing_response:

	# This boolean will disable the total score output 
	# For the first run of the program if the user decides not to run the program
	first_time_bye_prompt = False

	# Default variables that refresh after every iteration
	ignore_prompt = False
	chose_gamemode = False

	# This integer variable controls the gamemode
	# '1' represents solo mode and '2' represents the vs. ai mode
	gamemode_type = 0
	
	# The initial value of the turns variable that defaults every new game
	game_turns = 0
	
	# THe initial value of the board number variable that defaults every game
	board_num = 0

	# Outputs the game number with an underline under every game
	print("Game: " + str(game_num))
	print("========")
	print("")

	# Collects and chooses the gametype based on the user command
	# This prompt will continue to run until the user inputs an accepted input
	while chose_gamemode != True:
		gamemode = input("Which level would you want to play? ('solo' or 'AI'): ").lower().strip()
		
		# Looks for the keyword solo in the user input to choose the correct gamemode
		if "solo" in gamemode:

			# Sets the gamemode to 1 which is solo mode
			gamemode_type = 1
			chose_gamemode = True
			print("")

		# Looks for the keyword ai in the user input to choose the correct gamemode
		elif "ai" in gamemode:

			# Sets the gamemode to 2 which is vs ai mode
			gamemode_type = 2
			chose_gamemode = True
			print("")

		# In the case that the user inputs a command that is not known
		# The prompt will continue to display
		else: 
			print("That is not a valid value, please re-enter")
			print("")

	# Takes in the user input for the board
	while board_num == 0:
		
		# In the case of an value error it will ask the user for new appropriate input
		try:
			board_num = int(input("Which initial board do you want to use(1,2 or 3): "))
			
			# This statement checks for specific integers '1' '2' and '3'
			# For the corresponding boards that the user chooses
			if board_num == 1 or board_num == 2 or board_num == 3:
				print("")

			# If the user enters in a non-number input
			# It will output to the user that an invalid non-number was inputed
			else:
				print("That is not a valid value, please re-enter")
				print("")
				board_num = 0

		# In the case of a value error it will output to the user that
		# The required input can only use integers that fit the restriction			
		except ValueError:
			print("The value should only have digits, please re-enter")
			print("")
			board_num = 0

	# Converts the integer value back into a string
	board_num = str(board_num)

	# Open file depending on user's input
	if board_num == "1":
		# Get the first number in the file 
		board = open("board1.csv").readline().strip().replace(',', '')
	elif board_num == "2":
		# Get the first number in the file 
		board = open("board2.csv").readline().strip().replace(',', '')
	elif board_num == "3":
		# Get the first number in the file 
		board = open("board3.csv").readline().strip().replace(',', '')

	# Print the messages before the initial board
	print("The board is")
	print("-------------")
	print("")
	print("(initial board)")
	print("")
	# Set the inital board data to a variable, board_data
	board_data = createBoardImages.create_initial_board(board_num)
	print("")
	# Set the first number in the board file to the dimensions
	board_dimensions = int(board)
	# Set the max to the length minus one
	the_max = board_dimensions - 1
	# Initialize the turns to 0
	turns = 0
	# Takes in the user input for the board
	while game_turns != "found":
		# In the case that the user enters a non-integer in the input
		# It will redirect the user to the exception prompt
		try:
			# Ask for the number of turns and change to an integer
			print("How many turns would you like to play? ")
			turns = int(input("( >= 0 and <= " + str(the_max)+ "): "))
			# If input is between 0 and the max then continue
			if turns == 0:
				ignore_prompt = True
				print("I see that you liked the board and you don't want changes!")
			if turns <= the_max and turns >= 0:
				game_turns = "found"
			# If input is not valid then loop
			else:
				print("That is not a valid value, please re-enter")
				print("")
		# Displays the error message then loops
		except ValueError:
			print("")
			print("The value should only have digits, please re-enter")
	print("")

	# Instructs the user to input a value in their position of choice
	# And lets the user know how to end their round without using all their turns
	if ignore_prompt != True:
		print("User, where do you want your digit? (-1 if you want no more turns)")
	
	# This part of the program runs if the chosen gametype is solo
	if gamemode_type == 1:
		# Initializes the counter variable for the turn number 
		# And a counter variable 
		counter = 0
		turn_num = 0
		# Sets this initial value of the boolean to False
		# If the value of the boolean is True it will not ask the user for any input
		# For the row, column, and value and print the new board without any changes
		blockage = False
		# Will continue to run until all the turns are used
		# Or if the user enters -1 to finish their round earlier
		while counter < turns:
			# In the case that the statement is not blocked it will ask the user for input
			if blockage != True:
				# Asks the user for the input for the row number
				draft_user_row = int(input("row?  (>=0 and <= " + str(the_max) + "): "))
				# If the user enters -1 it will block all statements in the turns block 
				if draft_user_row == -1:
					counter = turns
					blockage = True
				# Until the user enters a row number that is accepted
				# It will output an error message and ask for new input
				else:
					while draft_user_row > the_max or draft_user_row < 0:
						print("That is not a valid value, please re-enter")
						draft_user_row = int(input("row?  (>=0 and <= " + str(the_max) + "): "))
					user_row = draft_user_row

			# In the case that the statement is not blocked it will ask the user for input
			if blockage != True:
				# Asks the user for the input for the column number
				draft_user_col = int(input("col?  (>=0 and <= " + str(the_max) + "): "))
				# If the user enters -1 it will block all statements in the turns block 
				if draft_user_col == -1:
					counter = turns
					blockage = True
				# Until the user enters a column number that is accepted
				# It will output an error message and ask for new input
				else:
					while draft_user_col > the_max or draft_user_col < 0:
						print("That is not a valid value, please re-enter")
						draft_user_col = int(input("col?  (>=0 and <= " + str(the_max) + "): "))
					user_col = draft_user_col

			# In the case that the statement is not blocked it will ask the user for input
			if blockage != True:
				draft_value = int(input("digit (0 to 9): "))
				# If the user enters -1 it will block all statements in the turns block 
				if draft_value == -1:
					counter = turns
					blockage = True
				# Until the user enters a value to insert that is accepted
				# It will output an error message and ask for new input
				else:
					while draft_value > 9 or draft_value < 0:
						print("That is not a valid value, please re-enter")
						draft_value = int(input("digit (0 to 9): "))
					value = draft_value

			# Outputs and formats the board and indicate to the user their command
			print("")		
			print("The board is")
			print("-------------")
			print("")
			print("(after user played)")
			print("")

			# In the case that the statement is not blocked it will print the board
			# Prints the board with the new command from the user
			if blockage != True:
				turn_num += 1
				board_data[user_row][user_col] = value
				createBoardImages.printBoard(board_data)
			# This statement runs when the turns was stopped by the user
			# And prints out the board without any further changes made
			else:
				createBoardImages.printBoard(board_data)
			counter += 1
			# In the case that the statement is not blocked through input: -1
			# It will output to the user that the maximum turns have been used
			if blockage != True and counter == turns:
				print("You reached the maximum turns possible, the game is over!")

	# This part of the program runs if the chosen gametype is vs. ai
	elif gamemode_type == 2:
		# The default values of the integers for the original turn number
		# And the changing value of the turns that indicates how long to loop
		turn_num = 0
		counter = 0
		# Sets the blockage boolean to False to make sure the input statements print
		# Unless the user manually entered -1 to stop the turns function early
		blockage = False
		# Will continue to run until all the turns are used
		# Or if the user enters -1 to finish their round earlier
		while counter < turns:
			# In the case that the statement is not blocked it will ask the user for input
			if blockage != True:
				# Asks the user for an appropriate row number
				draft_user_row = int(input("row?  (>=0 and <= " + str(the_max) + "): "))
				# In the case that the user enters -1 for the input
				# Block all future inputs in the current iteration and end the loop
				if draft_user_row == -1:
					counter = turns
					blockage = True
				# This loop will continue asking for the row number until
				# An appropriate input that fits the requirements is inputed
				else:
					while draft_user_row > the_max or draft_user_row < 0:
						print("That is not a valid value, please re-enter")
						draft_user_row = int(input("row?  (>=0 and <= " + str(the_max) + "): "))
					user_row = draft_user_row

			# In the case that the statement is not blocked it will ask the user for input
			if blockage != True:
				draft_user_col = int(input("col?  (>=0 and <= " + str(the_max) + "): "))
				# In the case that the user enters -1 for the input
				# Block all future inputs in the current iteration and end the loop
				if draft_user_col == -1:
					counter = turns
					blockage = True
				# This loop will continue asking for the column number until
				# An appropriate input that fits the requirements is inputed
				else:
					while draft_user_col > the_max or draft_user_col < 0:
						print("That is not a valid value, please re-enter")
						draft_user_col = int(input("col?  (>=0 and <= " + str(the_max) + "): "))
					user_col = draft_user_col

			# In the case that the statement is not blocked it will ask the user for input
			if blockage != True:
				draft_value = int(input("digit (0 to 9): "))
				# If the user enters -1 it will block all statements in the turns block 
				if draft_value == -1:
					counter = turns
					blockage = True
				# Until the user enters a value to insert that is accepted
				# It will output an error message and ask for new input
				else:
					while draft_value > 9 or draft_value < 0:
						print("That is not a valid value, please re-enter")
						draft_value = int(input("digit (0 to 9): "))
						print("")
					value = draft_value
			
			# In the case that the statement is not blocked it will format the board
			if blockage != True:	
				print("The board is")
				print("-------------")
				print("")
				print("(after user played)")
				print("")

				# In the case that the statement is not blocked it will print the board
				# With the users commands entered in the outputed board
				if blockage != True:
					board_data[user_row][user_col] = value
					createBoardImages.printBoard(board_data)
					turn_num += 1
				# If it is the case that the statement is blocked
				# It will print the board without any further changes to the board
				else:
					createBoardImages.printBoard(board_data)

				# Indicates to the user that the ai will now play their turn
				print("The computer will play now!")
				# And gives notice to the user before outputing the computers command
				input("Hit return to continue... ")

				# Using the random function
				# The position number and value is selected as the computers command
				ai_rownum = random.randint(0, the_max)
				ai_colnum = random.randint(0, the_max)
				ai_value = random.randint(0, 9)

				# Formats the board by outputing the new board
				print("")
				print("The board is")
				print("-------------")
				print("")
				# Displays where the computer commanded their turn to the user
				print(("after computer played in row: " + str(ai_rownum) + " and col: " + str(ai_colnum)))
				print("")

				# Saves the changes of the ai to the new printboard
				board_data[ai_rownum][ai_colnum] = ai_value
				# And outputs the board to the user
				createBoardImages.printBoard(board_data)
				counter += 1

			# In the case that the statement is not blocked through input: -1
			# It will output to the user that the maximum turns have bene used
			if blockage != True and counter == turns:
				print("You reached the maximum turns possible, the game is over!\n")

	# Initialize the sum lists
	sumOfCol = []
	sumOfRow = []
	# Create the lists of the sums of the column and the row
	createBoardImages.listOfCol(board_data, sumOfCol)
	createBoardImages.listOfRow(board_data, sumOfRow)

	# Initialize total value of row and column
	total_col = 0
	total_row = 0
	combined_list = []

	# Combine the sum lists together
	for i in range(board_dimensions):
		combined_list.append(sumOfRow[i])
		combined_list.append(sumOfCol[i])

	# Set the highest number in the list to a variable, largest
	largest = createBoardImages.find_max(combined_list)

	# If there were 0 turns in the game then divide by 1
	if turn_num == 0:
		turn_num = 1
	
	# Get the round score by dividing the largest number 
	# by the number of turns played
	current_round_score = (int(largest))//(int(turn_num))

	# Tell the user the points
	print("Totals for this game")
	print("--------------------")
	print("")
	print("The 'final line' with the sum of all columns is: " + str(sumOfCol))
	print("The 'final column' with the sum of all rows is: " + str(sumOfRow))
	print("")
	print("The points resulting from this board are: " + str(current_round_score))
	print("Points were calculated as:")
	print("  the maximum of all numbers in the final line and column (" + str(largest) + ")")
	print("  divided by the number of turns played (" + str(turn_num) + ")")
	print("")

	# Initialize the counter for odd numbers
	num_times_odd = 0
	# Check each index in both lists
	for number_in_slot in range(board_dimensions):
		# If the index is even then pass
		if sumOfCol[number_in_slot]%2 == 0 and sumOfRow[number_in_slot]%2 == 0:
			pass
		# If the index is odd, add to the counter
		else:
			num_times_odd += 1

	# If the number of odds is zero then user wins
	if num_times_odd == 0:
		user_score += 1
		# Add the current score to the total score
		total_score += current_round_score
		print("Yey! User, you won this game!")
		print("All numbers in the final line and column are even!")
		print("You will be added " + str(current_round_score) + " points to your total")
		print("Your points so far are: " + str(total_score))
		print("")
	# If the number of odds is greater than zero 
	# then the computer wins
	else:
		computer_score += 1
		# Subtract the current score from the total score
		total_score -= current_round_score
		print("So sorry, User, you lost this game!")
		print("Not all sums in the final line and column are even!")
		print("You will be substracted " + str(current_round_score) + " points from your total")
		print("Your points so far are: " + str(total_score))
		print("")
	
	# Ask the user for the length of the final images
	print("In preparation for the images for the final line and column...")
	print("How many pixels (columns) would you like per square? (recommend <= 60)")
	# Ask the user for the length of the final image and change it to an integer
	length = int(input("Number of pixels-->  "))
	# If length is greater than 60 ask again
	while length > 60:
		print("That is not a valid value, please re-enter")
		length = int(input("Number of pixels-->  "))
	input("Hit return to continue...")
	# Show the image and save the image
	cmpt120imageWeek9.showImage(createBoardImages.listColImage(sumOfCol, length), "Final line")
	cmpt120imageWeek9.saveImage(createBoardImages.listColImage(sumOfCol, length), "imgLine "+str(game_num)+".jpg")
	input("Hit return to continue...")
	# Show the image and save the image
	cmpt120imageWeek9.showImage(createBoardImages.listRowImage(sumOfRow, length), "Final Column")
	cmpt120imageWeek9.saveImage(createBoardImages.listRowImage(sumOfRow, length), "imgCol "+str(game_num)+".jpg")

	print("")
	# Ask the user if they would like to play again
	continue_playing = input("Would you like to play again? (y/n): ").lower()
	# Check if they want to play again
	while playing == True:
		# If yes break out of loop
		if continue_playing == "y":
			print("")
			# Break out of loop
			playing = False
		# If no set the variable to no
		elif continue_playing == "n":
			print("")
			# Break out of loop
			playing = False
			playing_response = "n"
		# Else ask user to re-enter
		else:
			print("Unrecognized response, please try again with (y/n).")
			print("")
			continue_playing = input("Would you like to play again? (y/n): ").lower()


	# Reset the playing variable to True to enable the prompt on the second game
	# And update the game number by increasing the number by one
	playing = True
	game_num += 1

# If they don't want to play again print the results
if 'n' == playing_response:
	if first_time_bye_prompt != True:
		print("TOTALS ALL GAMES")
		print("Total points user in all games:	" + str(total_score))
		print("Total games the user won:  " + str(user_score))
		print("Total games the computer won:  " + str(computer_score))
		print("")
	print("Bye!!")

# Else ask user to re-enter
else:
	print("Sorry, your command was not recognized")
	print("If you want to try again, please consider pressing RUN")