"""
Play
High Scores
Settings
Credits
Exit
"""

import msvcrt
import os
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
		self.menulist = ["Play","Instructions","High Scores","Settings","Credits","Exit"]
		self.currentSelection = 0

	def play(self):
		pass

	def highscore(self):
		pass

	def settings(self):
		pass

	def credits(self):
		pass

	def exit(self):
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
		os.system("cls")


		for listIndex, option in enumerate(self.menulist):
			if listIndex == currentSelection:
				print(color.SELECT + color.BLACK + option + color.BASE)
			else:
				print(option)
		#test



	def handle_input(self):
		# print("handled input")
		key_stroke = msvcrt.getch()
		try:
			key_stroke = (str(key_stroke, 'utf-8'))
		except UnicodeDecodeError as e:
			self.handle_input()

		

		keylist = {"w":-1,"s":+1}

		if key_stroke in keylist:
			self.move(keylist[key_stroke])  # Research fetching from dictionary
			# if neither, screen will clear -- fix

	def update(self):
		# print(update)
		print('')

		self.handle_input()
		print(os.get_terminal_size())




menu = UI()
while True:
	if msvcrt.kbhit():
		menu.update()