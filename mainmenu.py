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
import pickle
import minewalker
import cursor
cursor.hide()

# Simple class that stores ANSI Escape characters for specific colours
class color:
	BOLD = '\u001b[1m'
	UNDERLINE = '\u001b[4m'
	SELECT = '\033[47m'
	BASE = '\033[0m'
	RED = '\033[91m'
	YELLOW = ''
	BLACK = '\033[30m'
	GREEN = '\033[92m'


keylog = []
sel = 0

def cls():
		os.system("cls")

def print_list(menulist):
	listIndex = 0

	width= os.get_terminal_size().columns
	half = width/2

	# TODO: Call cls right before printing to remove flicker
	# toBePrinted = []

	cls()

	# Add padding to center menu items
	for listIndex, option in enumerate(menulist):
		blankchars = half - len(option)/2
		chars = ""
		for x in range(int(blankchars)):
			chars += " "
		
		# Highlight selected menu lists
		if listIndex ==sel:
			print((chars + color.SELECT + color.BLACK + option + color.BASE))
		else:
			print((chars + option))

	# Function that moves the current selection through the menu list
def move_list(direction, menulist):
	print("yes")

	# Copy instance variable to a local var and add the direction 
	currentSelection = sel
	currentSelection += direction

	# Conditions to prevent menu list from wrapping around 
	if currentSelection > len(menulist)-1:
		currentSelection -= 1
	elif currentSelection < 0:
		currentSelection += 1

	currentSelection = sel
	print_list(menulist)


def capture_input():

	key_stroke = msvcrt.getch()
	if ord(key_stroke) == 224:
		key = ord(msvcrt.getch())
		if key == 80:
			key_stroke = b's'
		elif key == 72:
			key_stroke = b'w'
		elif key == 75:
			key_stroke = b'a'
		elif key == 77:
			key_stroke = b'd'
		else:
			pass
	try:
		key_stroke = (str(key_stroke, 'utf-8'))
	except UnicodeDecodeError:
		pass

	keylog.append(key_stroke)
	return key_stroke

def main_menu():
	items = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
	# print_list(items)
	keylist = {"w":-1, "s":+1}
	while True:
		if msvcrt.kbhit():
			key = capture_input()
			print(key)
			print(sel)
			if key in keylist:
				time.sleep(0.2)
				print("hello?")
				move_list(keylist[key],items)

main_menu()




# Main menu UI object
# class UI(object):

# 	def __init__(self):
# 		self.keylog = []
# 		self.menulist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
# 		self.functionlist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
# 		self.currentSelection = 0

# 	# Functions for each of the menu items
# 	def cls(self, type = 0):
# 		os.system("cls")


# 	def play(self):
# 		self.cls()
# 		mygame = minewalker.Game()
# 		mygame.run()
# 		self.handle_input()

# 	def instructions(self):
# 		# self.cls()



# 		instructions = """Welcome to MineWalker!\n\n{0}Objective:{1}
# 		\nReach the end column of the minefield without setting off any mines.\n
# 		\n{2}How to Play:{3}
# 		\nThe position of each mine will be shown to you for a small amount of time depending on your level of difficulty.
# 		\nRemember where the mines are and navigate the minefield using W A S D to get to the end column.\n
# 		\n{4}Special Abilities:{5}
# 		\nQ --> Scan for mines around you
# 		\nE --> Throw a blanket to any location and detonate any mines to make those squares safe for future travel""".format(color.UNDERLINE, color.BASE, color.UNDERLINE, color.BASE, color.UNDERLINE, color.BASE)
# 		print(instructions)
# 		print("\n\n[ Press ANY KEY to Return to Main Menu ]")
# 		self.handle_input()

# 	def leaderboard(self):
# 		print("kea")

# 	def settings(self):
# 		self.currentSelection = 0
# 		menulist = ["Choose your player character: ", "Choose your mine character: ", "Choose your path character: ", "Choose your box character: "]
# 		self.handle_input(menulist)


# 	def credits(self):
# 		pass

# 	def exit(self):
# 		sys.exit("Thank you for playing my game!")
# 		pass

# 	def main_menu(self):

# 		key_stroke = self.keylog[-1]

# 		menulist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
# 		self.functionlist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]

# 		dispatch = ["self." + menuitem.lower() for menuitem in functionlist]

# 		if key_stroke == "\r" or key_stroke == " ":
# 			self.cls()
# 			eval(dispatch[self.currentSelection])()

# 		elif key_stroke in keylist:
# 			self.move_list(keylist[key_stroke],menulist) 

# 	def throwaway(self):
# 		pass
# 	def print_list(self, menulist):
# 		listIndex = 0

# 		width= os.get_terminal_size().columns
# 		half = width/2

# 		# TODO: Call cls right before printing to remove flicker
# 		# toBePrinted = []
		
# 		self.cls()
# 		# Add padding to center menu items
# 		for listIndex, option in enumerate(menulist):
# 			blankchars = half - len(option)/2
# 			chars = ""
# 			for x in range(int(blankchars)):
# 				chars += " "
			
# 			# Highlight selected menu lists
# 			if listIndex == self.currentSelection:
# 				print((chars + color.SELECT + color.BLACK + option + color.BASE))
# 			else:
# 				print((chars + option))

# 	# Function that moves the current selection through the menu list
# 	def move_list(self, direction, menulist):

# 		# Copy instance variable to a local var and add the direction 
# 		currentSelection = self.currentSelection
# 		currentSelection += direction

# 		# Conditions to prevent menu list from wrapping around 
# 		if currentSelection > len(menulist)-1:
# 			currentSelection -= 1
# 		elif currentSelection < 0:
# 			currentSelection += 1

# 		self.currentSelection = currentSelection
# 		self.print_list(menulist)


# 	def capture_input(self):

# 		key_stroke = msvcrt.getch()
# 		if ord(key_stroke) == 224:
# 			key = ord(msvcrt.getch())
# 			if key == 80:
# 				key_stroke = b's'
# 			elif key == 72:
# 				key_stroke = b'w'
# 			elif key == 75:
# 				key_stroke = b'a'
# 			elif key == 77:
# 				key_stroke = b'd'
# 			else:
# 				pass
# 		try:
# 			key_stroke = (str(key_stroke, 'utf-8'))
# 		except UnicodeDecodeError:
# 			pass

# 		self.keylog.append(key_stroke)
# 		return key_stroke

# 	# def handle_input(self, menulist = []):

# 	# 	key_stroke = self.keylog[-1]

# 	# 	keylist = {"w":-1, "s":+1}

# 	# 	# Contains a list of all menu items with lowercase letters to match the specific functions created for them.
# 	# 	dispatch = ["self." + menuitem.lower() for menuitem in self.functionlist]

# 	# 	# If the handle input function is not called from update, clear the screen and default to the main menu list
# 	# 	if inspect.stack()[1][3] != "update":
# 	# 		self.currentSelection = 0
# 	# 		self.cls(1)
# 	# 		self.print_list(self.menulist)

# 	# 	# If Enter or Spacebar is pressed, the currently selected function from the menu list is called using eval
# 	# 	if key_stroke == "\r" or key_stroke == " ":
# 	# 		self.cls()
# 	# 		eval(dispatch[self.currentSelection])()

# 	# 	elif key_stroke in keylist:
# 	# 		self.move_list(keylist[key_stroke],menulist) 


# 	def update(self):
# 		self.capture_input()
# 		self.print_list(self.menulist)

# 		self.handle_input(self.menulist)





# menu = UI()
# menu.print_list(menu.menulist)

# while True:
# 	if msvcrt.kbhit():
		




'''
menu()
handle input, check input
move through menu items
selec items

settings()
handle input, check input
move thruogh items
select items
use input and change variables

menulist

if on minecharat == change mine 
if on path characr: change path





'''