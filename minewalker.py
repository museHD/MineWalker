import itertools
import pandas as pd
import numpy as np
from random import randint
import msvcrt
import time
import os, sys
import random

class color:
   GREEN = '\033[92m'
   BASE = '\033[0m'

class Game(object):

	def __init__(self):
		self.length = 10
		self.boxChar = "_"
		self.playerChar = "O"
		self.pathChar = "."
		self.mineChar = "#"
		self.nMines = 15
		self.displayInterval = 0.6
		self.path = []
		self.minePos = []

	# Takes a 2D array, converts it to a pandas df and prints it to display
	# TODO: Find out if the entire grid can be reprinted in console
	def print_grid(self, grid):
		# time.sleep(0.5)
		os.system("cls")
		# for i in range(9):
			
		df = pd.DataFrame(grid)
		# print(df)
		print(df.to_string(index=False, header=False).replace(self.playerChar, color.GREEN + self.playerChar + color.BASE))

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

	# Randomly set mines to the 
	def set_mines(self,grid):
		nMines = self.nMines
		for mines in range(nMines):
			mineX = random.randint(0,self.length-1)
			mineY = random.randint(0,self.length-1)
			grid[mineX][mineY] = self.mineChar
			self.minePos.append((mineX,mineY))


	def dfs(self, locations):
		if 

	# Currently does not work -- TODO: Implement DFS search 
	def verify_path(self):
		hidden = self.hidden_grid
		spotPath = []
		x = 0
		y = 0

		myPath = []
		# noPath = True
		toVisit = []
		for x in range(self.length):
			for y in range(self.length):
				toVisit.append((x,y))

		print(toVisit)
		for eachMine in self.minePos:
			if eachMine in toVisit:
				# print(eachMine)
				toVisit.remove(eachMine)


		# print("\n\n")
		# print(toVisit)
		# time.sleep(2)

		'''
		while noPath == True:
			if hidden[x+1][y] == self.mineChar:

				if hidden[x][y+1] == self.mineChar:

					print("DED")
					break
				y = y+1
			else:
				x = x+1
			point = (x,y)
			if x == self.length and y == self.length:
				noPath = False
				print(myPath)
				print("LES GO")
				break
			myPath.append(point)

		'''



	def game_state(self):
		state = "running"
		if self.hidden_grid[self.posX][self.posY] == self.mineChar:
			state = "lose"
			return state
		if self.posX == self.length-1 and self.posY == self.length-1:
			state = "win"
			return state
		return state


	def move_player(self, direction):


		# Implement Movelist input structure later

		# IMPLEMENTING MOVELIST
		direction = direction.lower()
		moveList = {"d":(0,1), "a":(0,-1), "w":(-1,0), "s":(1,0)}

		if direction in moveList:
			self.player_grid[self.posX][self.posY] = self.pathChar
			# self.myPath.append((self.posX, self.posY))
			addX, addY = moveList[direction]
			self.posX += addX
			self.posY += addY

			if self.posY == self.length:
				self.posY -= 1
			elif self.posY == -1:
				self.posY += 1
			if self.posX == self.length:
				self.posX -= 1
			elif self.posX == -1:
				self.posX += 1

			self.player_grid[self.posX][self.posY] = self.playerChar
			# self.player_grid[]

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
		self.set_mines(self.hidden_grid)
		self.print_grid(self.hidden_grid)
		self.player_grid = self.gen_grid()
		time.sleep(self.displayInterval)

		self.posX = 0
		self.posY = 0
		self.player_grid[self.posX][self.posY] = self.playerChar
		self.print_grid(self.player_grid)

		# self.verify_path()

		while self.game_state() == "running":
			if msvcrt.kbhit():
				self.capture_input()
				self.print_grid(self.player_grid)
				if self.game_state() == "lose":
					self.print_grid(self.hidden_grid)
					print("You stepped on a mine and set off all the others...")

				elif self.game_state() == "win":
					print("you win!")



		# REFER TO 
		"""import msvcrt
		while True:
		    if msvcrt.kbhit():
		        key_stroke = msvcrt.getch()
		        print(key_stroke)   # will print which key is pressed

		from https://www.codespeedy.com/how-to-detect-which-key-is-pressed-in-python/
		        """

# myGame = Game()
# myGame.run()


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