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


class color:
	SELECT = '\033[47m'
	BASE = '\033[0m'
	RED = '\033[91m'
	YELLOW = ''
	BLACK = '\033[30m'
	GREEN = '\033[92m'

class UI(object):

	def __init__(self):
		self.menulist = ["Play","Instructions","Leaderboard","Settings","Credits","Exit"]
		self.currentSelection = 0

	def play(self):
		print("WE ARE NOW PLAYING")
		time.sleep(2)

	def instructions(self):
		pass

	def leaderboard(self):
		pass

	def settings(self):
		pass

	def credits(self):
		pass

	def exit(self):
		sys.exit("Thank you for playing my game!")
		pass

	def move(self, direction):

		currentSelection = self.currentSelection
		currentSelection += direction

		if currentSelection > len(self.menulist)-1:
			currentSelection -= 1
		elif currentSelection < 0:
			currentSelection += 1

		# print(currentSelection)
		self.currentSelection = currentSelection
		# print(currentSelection)

		listIndex = 0

		width, throw = os.get_terminal_size()
		# print(width)
		half = width/2

		os.system("cls")



		for listIndex, option in enumerate(self.menulist):
			blankchars = half - len(option)/2
			chars = ""
			for x in range(int(blankchars)):
				chars += " "
			
			if listIndex == currentSelection:
				print(chars + color.SELECT + color.BLACK + option + color.BASE)
			else:
				print(chars + option)

		#test



	def handle_input(self):
		# print("handled input")
		key_stroke = msvcrt.getch()

		keylist = {"w":-1, "s":+1} #"\r":select, " ":select}

		if key_stroke in keylist:
			self.move(keylist[key_stroke])
		else:
			pass
		try:
			key_stroke = (str(key_stroke, 'utf-8'))

		except UnicodeDecodeError as e:
			self.handle_input()

		# use eval 
		# use 
		dispatch = ["self." + menuitem.lower() for menuitem in self.menulist]

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
