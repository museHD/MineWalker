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



#Main menu UI object
class UI(object):

	def __init__(self):
		self.keylog = []
		self.menulist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
		self.functionlist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
		self.currentSelection = 0
		self.mygame = minewalker.Game()

	# Functions for each of the menu items
	def cls(self, type = 0):
		os.system("cls")

	def wait(self):
		while True:
			if msvcrt.kbhit():
				msvcrt.getch()
				return 0
	def play(self):
		self.cls()
		self.mygame.run()
		print("Would you like to play again?")
		option_list = ["Yes", "No"]
		self.move_list(option_list,cls=False)
		

	def instructions(self):
		# self.cls()
		instructions = """Welcome to MineWalker!\n\n{0}Objective:{1}
		\nReach the end column of the minefield without setting off any mines.\n
		\n{2}How to Play:{3}
		\nThe position of each mine will be shown to you for a small amount of time depending on your level of difficulty.
		\nRemember where the mines are and navigate the minefield using W A S D to get to the end column.\n
		\n{4}Special Abilities:{5}
		\nQ --> Scan for mines around you
		\nE --> Throw a blanket to any location and detonate any mines to make those squares safe for future travel""".format(color.UNDERLINE, color.BASE, color.UNDERLINE, color.BASE, color.UNDERLINE, color.BASE)
		print(instructions)
		print("\n\n[ Press ANY KEY to Return to Main Menu ]")
		self.wait()
		return 0


		

	def leaderboard(self):
		print("kea")
		self.wait()
		return 0

	def settings(self):
		self.currentSelection = 0

		playerChar = self.mygame.playerChar
		mineChar = self.mygame.mineChar
		pathChar = self.mygame.pathChar
		boxChar = self.mygame.boxChar	

		menulist = [f"Choose your player character: {playerChar}", f"Choose your mine character: {mineChar}", f"Choose your path character: {pathChar}",
		f"Choose your box character: {boxChar}", "Save Changes", "Reset to Defaults", "Return to Main Menu"]
		self.print_list(menulist)
		# select = True
		characterList = [playerChar, mineChar, pathChar, boxChar]
		gameCharList = [self.mygame.playerChar, self.mygame.mineChar, self.mygame.pathChar, self.mygame.boxChar]
		runSettings = True

		def reset(characterList):
			# print(selIndex)
			# print("rests")
			playerChar = "O"
			mineChar = "#"
			pathChar = "."
			boxChar = "_"
			characterList = [playerChar, mineChar, pathChar, boxChar]
			# print(characterList)
			self.mygame.playerChar = characterList[0]
			self.mygame.mineChar = characterList[1]
			self.mygame.pathChar = characterList[2]
			self.mygame.boxChar	= characterList[3]
			return characterList

		while runSettings:
			select = False

			if self.move_list(menulist) == 0:

				self.print_list(menulist)
				selIndex = self.currentSelection

				# Return
				if selIndex == len(menulist)-1:
					runSettings = False
					return 0

				# Reset to Default
				elif selIndex == len(menulist)-2:
					characterList = reset(characterList)

				# Save Changes
				elif selIndex == len(menulist)-3:

					for eachChar in characterList:
						if characterList.count(eachChar)>1:
							print("\nPlease Enter separate, valid characters!")
							time.sleep(1.3)
							characterList = reset(characterList)
						else:
							self.mygame.playerChar = characterList[0]
							self.mygame.mineChar = characterList[1]
							self.mygame.pathChar = characterList[2]
							self.mygame.boxChar	= characterList[3]

				else:
					select = True
				while select == True:
					if msvcrt.kbhit():
						char = self.capture_input()[0]
						menulist[selIndex] = menulist[selIndex][:-1] + str(char)
						print(selIndex)
						characterList[selIndex] = char
						select = False

				for i in range(4):
					# print('yes')
					# time.sleep(0.2)
					# print(menulist)
					# print(characterList)
					menulist[i] = menulist[i][:-1] + characterList[i]

				self.print_list(menulist)



	def credits(self):
		pass

	def exit(self):
		sys.exit("Thank you for playing my game!")
		pass

	def print_list(self, menulist, cls = True):
		listIndex = 0
		# clear = '\033[{0}A'.format(len(menulist)+1)
		width= os.get_terminal_size().columns
		half = width/2

		# TODO: Call cls right before printing to remove flicker
		# toBePrinted = []
		if cls:
			self.cls()
		# print(clear)
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

	# Gets keystrokes (and arrows) and returns a single string
	def capture_input(self):

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

		self.keylog.append(key_stroke)
		return key_stroke


	# Function that moves the current selection through the menu list
	def move_list(self, menulist, cls = True):
		keylist = {"w":-1, "s":+1}
		scroll = True


		while scroll == True:
			if msvcrt.kbhit():
				key_stroke = self.capture_input()


				if key_stroke == "\r" or key_stroke == " ":
					if cls == True:
						self.cls()
					scroll = False
					return 0

				
				elif key_stroke in keylist:
					direction = (keylist[key_stroke])

				# Copy instance variable to a local var and add the direction 
					currentSelection = self.currentSelection
					currentSelection += direction

					# Conditions to prevent menu list from wrapping around 
					if currentSelection > len(menulist)-1:
						currentSelection -= 1
					elif currentSelection < 0:
						currentSelection += 1

					self.currentSelection = currentSelection

				self.print_list(menulist,cls)



	# def handle_input(self, menulist = []):

	#   key_stroke = self.keylog[-1]

	#   keylist = {"w":-1, "s":+1}

	#   # Contains a list of all menu items with lowercase letters to match the specific functions created for them.
	#   dispatch = ["self." + menuitem.lower() for menuitem in self.functionlist]

	#   # If the handle input function is not called from update, clear the screen and default to the main menu list
	#   if inspect.stack()[1][3] != "update":
	#       self.currentSelection = 0
	#       self.cls(1)
	#       self.print_list(self.menulist)

	#   # If Enter or Spacebar is pressed, the currently selected function from the menu list is called using eval
	#   if key_stroke == "\r" or key_stroke == " ":
	#       self.cls()
	#       eval(dispatch[self.currentSelection])()

	#   elif key_stroke in keylist:
	#       self.move_list(keylist[key_stroke],menulist) 

	def main_menu(self):
		mainlist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]        
		dispatch = ["self." + menuitem.lower() for menuitem in mainlist]

		if self.move_list(mainlist) == 0:
			if eval(dispatch[self.currentSelection])() == 0:
				self.currentSelection = 0
				self.print_list(mainlist)
				return 0
	

	def update(self):
		self.capture_input()
		# self.print_list(self.menulist)


menu = UI()
menu.print_list(menu.menulist)


while True:
	if msvcrt.kbhit():
		menu.main_menu()
	


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