"""
Play
High Scores
Settings
Credits
Exit
"""

import msvcrt
import os, sys
import time

# Simple class that stores ANSI Escape characters for specific colours
class color:
	SELECT = '\033[47m'
	BASE = '\033[0m'
	RED = '\033[91m'
	YELLOW = ''
	BLACK = '\033[30m'
	GREEN = '\033[92m'

# Main menu UI object
class UI(object):

	def __init__(self):
		self.menulist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
		self.currentSelection = 0

	# Functions for each of the menu items

	def play(self):
		print("WE ARE NOW PLAYING")
		time.sleep(2)

	def instructions(self):
		print("instructions")

	def leaderboard(self):
		print("kea")

	def settings(self):
		pass

	def credits(self):
		pass

	def exit(self):
		sys.exit("Thank you for playing my game!")
		pass

	# Function that moves the current selection through the menu list
	def move(self, direction):

		# Copy instance variable to a local var and add the direction 
		currentSelection = self.currentSelection
		currentSelection += direction

		# Conditions to prevent menu list from wrapping around 
		if currentSelection > len(self.menulist)-1:
			currentSelection -= 1
		elif currentSelection < 0:
			currentSelection += 1

		self.currentSelection = currentSelection
		# print(currentSelection)

		listIndex = 0

		width= os.get_terminal_size().columns
		half = width/2

		# TODO: Call cls right before printing to remove flicker

		os.system("cls")

		# Add padding to center menu items
		for listIndex, option in enumerate(self.menulist):
			blankchars = half - len(option)/2
			chars = ""
			for x in range(int(blankchars)):
				chars += " "
			
			# Highlight selected menu lists
			if listIndex == currentSelection:
				print(chars + color.SELECT + color.BLACK + option + color.BASE)
			else:
				print(chars + option)

		#test



	def handle_input(self):
		# print("handled input")

		key_stroke = msvcrt.getch()
		keylist = {"w":-1, "s":+1}

		# Try sending keystroke to the move function without encoding it to utf-8. Might be useful for arrow key implementation later
		if key_stroke in keylist:
			self.move(keylist[key_stroke])
		else:
			pass
		try:
			key_stroke = (str(key_stroke, 'utf-8'))
		except UnicodeDecodeError as e:
			self.handle_input()

		# Contains a list of all menu items with lowercase letters to match the specific functions created for them.
		dispatch = ["self." + menuitem.lower() for menuitem in self.menulist]


		# If Enter or Spacebar is pressed, the currently selected function from the menu list is called using eval
		if key_stroke == "\r" or key_stroke == " ":
			eval(dispatch[self.currentSelection])()



		if key_stroke in keylist:
			self.move(keylist[key_stroke])  # Research fetching from dictionary
			# if neither, screen will clear -- fix

	def update(self):
		self.handle_input()





menu = UI()
while True:
	if msvcrt.kbhit():
		menu.update()
