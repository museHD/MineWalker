import itertools
import pandas as pd
import numpy as np
from random import randint
import msvcrt
import time
import os, sys


class Game(object):

	def __init__(self):
		self.length = 10
		self.boxChar = ""

	# Takes a 2D array, converts it to a pandas df and prints it to display
	# TODO: Find out if the entire grid can be reprinted in console
	def print_grid(self, grid):
		# time.sleep(0.5)
		os.system("cls")
		# for i in range(9):
			
		df = pd.DataFrame(grid)
		# print(df)
		print(df.to_string(index=False, header=False))

	# Generates a simple 2d array
	def gen_grid(self):

		grid = []
		thisRow = []

		# Box character 
		self.boxChar = "_"

		# Populates a 2D array with box characters
		for yCols in range(self.length):
			for xRows in range(self.length):
				thisRow.append(self.boxChar)
			grid.append(thisRow)
			thisRow = []
		return grid

	def move_player(self, direction):

		# print("pos")
		try:

			if direction == "d":
				# print('ey')
				self.player_grid[self.posX][self.posY] = "_"
				self.posX += 0
				self.posY += 1
				# self.player_grid[self.posX][self.posY] = "o"
			elif direction == "a":
				self.player_grid[self.posX][self.posY] = "_"
				self.posX += 0
				self.posY -= 1
				# self.player_grid[self.posX][self.posY] = "o"
			elif direction == "w":
				self.player_grid[self.posX][self.posY] = "_"
				self.posX -= 1
				self.posY += 0
				# self.player_grid[self.posX][self.posY] = "o"
			elif direction == "s":
				self.player_grid[self.posX][self.posY] = "_"
				self.posX += 1
				self.posY += 0
				# self.player_grid[self.posX][self.posY] = "o"

			if self.posY == self.length:
				self.posY -= 1
			elif self.posY == -1:
				self.posY += 1
			if self.posX == self.length:
				self.posX -= 1
			elif self.posX == -1:
				self.posX += 1

			self.player_grid[self.posX][self.posY] = "o"

		except IndexError:
			if self.posY == self.length:
				self.posY -= 1

	def capture_input(self): 
		key_stroke = msvcrt.getch()
	# try:
		key_stroke = (str(key_stroke, 'utf-8'))
		# print(key_stroke)
		self.move_player(key_stroke)


	# except:
	# 	pass

	def run(self):
		run = True 

		self.hidden_grid = self.gen_grid()
		self.player_grid = self.gen_grid()

		self.posX = 0
		self.posY = 0
		self.player_grid[self.posX][self.posY] = "o"
		self.print_grid(self.player_grid)

		while run:
			if msvcrt.kbhit():
				self.capture_input()
				self.print_grid(self.player_grid)


		# REFER TO 
		"""import msvcrt
		while True:
		    if msvcrt.kbhit():
		        key_stroke = msvcrt.getch()
		        print(key_stroke)   # will print which key is pressed

		from https://www.codespeedy.com/how-to-detect-which-key-is-pressed-in-python/
		        """

myGame = Game()
myGame.run()


""" SNIPPET using numpy """
# def print_array(array):
# 	for y in range(len(array)):
# 		for x in range(len(array)):
# 			print(array[x][y])

# # board = np.array([rows,cols])
# board = np.random.randint(1,100,(10,10))
# print(board)
# # print(' '.join(str(n) for n in board))
# print_array(board)