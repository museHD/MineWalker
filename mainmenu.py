"""
Play
High Scores
Settings
Credits
Exit
"""

import msvcrt
import os, sys, inspect
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
	def cls(self):
		os.system("cls")

	def play(self):
		print("WE ARE NOW PLAYING")

	def instructions(self):
		self.cls()

		instructions = """Welcome to MineWalker!\n\nObjective:
		\nReach the end column of the minefield without setting off any mines.\n
		\nHow to Play:
		\nThe position of each mine will be shown to you for a small amount of time depending on your level of difficulty.
		\nRemember where the mines are and navigate the minefield using W A S D to get to the end column.\n
		\nSpecial Abilities:
		\nQ --> Scan for mines around you
		\nE --> Throw a blanket to any location and detonate any mines to make those squares safe for future travel"""
		print(instructions)
		print("\n\n[  Press ANY KEY to Return to Main Menu  ]")
		self.handle_input()

	def leaderboard(self):
		print("kea")

	def settings(self):
		pass

	def credits(self):
		pass

	def exit(self):
		sys.exit("Thank you for playing my game!")
		pass

	def print_list(self, menulist):
		listIndex = 0

		width= os.get_terminal_size().columns
		half = width/2

		# TODO: Call cls right before printing to remove flicker
		# toBePrinted = []
		
		os.system("cls")
		# Add padding to center menu items
		for listIndex, option in enumerate(menulist):
			blankchars = half - len(option)/2
			chars = ""
			for x in range(int(blankchars)):
				chars += " "
			
			# Highlight selected menu lists
			if listIndex == self.currentSelection:
				print((chars + color.SELECT + color.BLACK + option + color.BASE))
			else:
				print((chars + option))

	# Function that moves the current selection through the menu list
	def move_list(self, direction, menulist):

		# Copy instance variable to a local var and add the direction 
		currentSelection = self.currentSelection
		currentSelection += direction

		# Conditions to prevent menu list from wrapping around 
		if currentSelection > len(menulist)-1:
			currentSelection -= 1
		elif currentSelection < 0:
			currentSelection += 1

		self.currentSelection = currentSelection
		self.print_list(menulist)

		# print(currentSelection)



		#test



	def handle_input(self):
		# print("handled input")

		key_stroke = msvcrt.getch()
		keylist = {"w":-1, "s":+1}

		# Try sending keystroke to the move function without encoding it to utf-8. Might be useful for arrow key implementation later
		if key_stroke in keylist:
			self.move_list(keylist[key_stroke],self.menulist)
		else:
			pass
		try:
			key_stroke = (str(key_stroke, 'utf-8'))
		except UnicodeDecodeError as e:
			self.handle_input()

		# Contains a list of all menu items with lowercase letters to match the specific functions created for them.
		dispatch = ["self." + menuitem.lower() for menuitem in self.menulist]

		if inspect.stack()[1][3] != "update":
			self.print_list(self.menulist)

		# If Enter or Spacebar is pressed, the currently selected function from the menu list is called using eval
		elif key_stroke == "\r" or key_stroke == " ":
			eval(dispatch[self.currentSelection])()

		elif key_stroke in keylist:
			self.move_list(keylist[key_stroke],self.menulist) 



		 # Research fetching from dictionary
			# if neither, screen will clear -- fix

	def update(self):
		self.handle_input()





menu = UI()
while True:
	if msvcrt.kbhit():
		menu.update()


