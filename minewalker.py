# import itertools
import pandas as pd
# import numpy as np
from random import randint
import msvcrt
import time
import os, sys
import random
import copy

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
		self.nMines = 50
		self.displayInterval = 0.8
		self.path = []
		self.minePos = []
		self.scanChar = "*"


	def restrict(self, n, low, high):
		if n < low:
			n += (low - n)
		if n > high:
			n -= (n - high)
		return n
	# Takes a 2D array, converts it to a pandas df and prints it to display
	# TODO: Find out if the entire grid can be reprinted in console
	def print_grid(self, grid):
		# time.sleep(0.5)
		os.system("cls")
		print()

		df = pd.DataFrame(grid)
		# print(df)
		print(df.to_string(index=False, header=False).replace(self.playerChar, color.GREEN + self.playerChar + color.BASE))

	def update_grid(self, grid):

		print('\033[{0}A'.format(self.length+9))
			
		df = pd.DataFrame(grid)
		# print(df)
		print(df.to_string(index=False, header=False).replace(self.playerChar, color.GREEN + self.playerChar + color.BASE))

	# Generates a simple 2d array
	def gen_grid(self):

		grid = []
		thisRow = []

		# Populates a 2D array with box characters
		for yCols in range(self.length):
			for xRows in range(self.length):
				thisRow.append(self.boxChar)
			grid.append(thisRow)
			thisRow = []
		return grid

	# Randomly set mines to the 
	def set_mines(self,grid):
		self.minePos = []
		nMines = self.nMines
		gridMax = self.length-1
		self.minePos = set(self.minePos)
		while len(self.minePos) != nMines:
			mineX = random.randint(0,gridMax)
			mineY = random.randint(0,gridMax)

			# Ensure mines are not placed at the start or end positions
			while (mineX == 0 and mineY == 0) or (mineX == gridMax and mineY == gridMax):
				mineX = random.randint(0,gridMax)
				mineY = random.randint(0,gridMax)				
			grid[mineX][mineY] = self.mineChar
			self.minePos.add((mineX,mineY))


	def dfs(self, x = 0, y = 0):
		toVisit = self.toVisit
		self.hiddencopy = copy.copy(self.hidden_grid)
		self.hiddencopy = self.hidden_grid

		if x == -1:
			x += 1
		if y == -1:
			y +=1

		nextX = x+1
		nextY = y+1

		if nextX == self.length+1:
			x-=1
			nextX -=2
		if nextY == self.length+1:
			nextY -=2
			y-=1

		right = (x,nextY)
		down = (nextX,y)
		up = (x-1,y)
		left = (x, y-1)

		# tuple vs list optimisation
		options = (right, down, up, left)

		for option in options:
			# print(option)
			if option in toVisit:
				x,y = option
				toVisit.remove(option)
				# self.hiddencopy[x][y] = self.pathChar
				# self.update_grid(self.hiddencopy)
				# time.sleep(0.1)
				if x == self.length-1 and y == self.length-1:
					# print("FOUnd")
					# time.sleep(5)
					return 0
				else:
					if self.dfs(x,y) == 0:
						return 0
		return 1

	# Calls above DFS to find path
	def verify_path(self):
		# hidden = copy.copy(self.hidden_grid)
		hidden = self.hidden_grid
		spotPath = []
		x = 0
		y = 0

		myPath = []
		# noPath = True
		self.toVisit = []
		for x in range(self.length):
			for y in range(self.length):
				self.toVisit.append((x,y))

		# print(self.toVisit)
		for eachMine in self.minePos:
			if eachMine in self.toVisit:
				# print(eachMine)
				self.toVisit.remove(eachMine)
		if self.dfs() == 0:
			# print("YES")
			return True
		else:
			# print('no')
			return False

	def game_state(self):
		state = "running"
		if self.hidden_grid[self.posX][self.posY] == self.mineChar:
			state = "lose"
			return state
		if self.posX == self.length-1 and self.posY == self.length-1:
			state = "win"
			print("You Win!")
			print("Would you like to Play Again?")
			return state
		return state


	def move_player(self, direction):

		### BUG where path is drawn onto player at the edge


		# Implement Movelist input structure later

		# IMPLEMENTING MOVELIST
		direction = direction.lower()
		moveList = {"d":(0,1), "a":(0,-1), "w":(-1,0), "s":(1,0)}
		poslist = [(0,1),(0,-1),(-1,0),(1,0)]
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

		
		elif direction == "q":
			for scanPoint in poslist:
				addX, addY = scanPoint
				addX += self.posX
				addY += self.posY
				addX = self.restrict(addX,0,self.length-1)
				addY = self.restrict(addY,0,self.length-1)

				if (addX,addY) in self.minePos:
					self.player_grid[addX][addY] = self.scanChar
				else:
					self.player_grid[addX][addY] = self.pathChar

			up = self.posY-1
			down = self.posY+1
			left = self.posX-1
			right = self.posX+1

			if up < 0:
				up+=1
			if down == self.length:
				down -= 1
			if left < 0:
				left += 1
			if right == self.length:
				right+=1

			if self.hidden_grid[right][down] == self.mineChar:
				self.player_grid[right][down] = self.scanChar
			else:
				self.player_grid[right][down] = self.pathChar

			if self.hidden_grid[left][up] == self.mineChar:
				self.player_grid[left][up] = self.scanChar
			else:
				self.player_grid[left][up] = self.pathChar

			if self.hidden_grid[left][down] == self.mineChar:
				self.player_grid[left][down] = self.scanChar
			else:
				self.player_grid[left][down] = self.pathChar

			if self.hidden_grid[right][up] == self.mineChar:
				self.player_grid[right][up] = self.scanChar
			else:
				self.player_grid[right][up] = self.pathChar
			self.player_grid[self.posX][self.posY] = self.playerChar

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
			# print(key_stroke)
			self.move_player(key_stroke)
		except UnicodeDecodeError:
			pass

	# except:
	# 	pass

	def run(self):

		self.path = []
		self.minePos = []
		run = True

		self.hidden_grid = self.gen_grid()
		self.set_mines(self.hidden_grid)

		# Verify path, if it fails, keep generating grids till verified
		verified = False
		while verified == False:
			if self.verify_path() == False:
				# print(self.toVisit)
				# verified+=1
				# print(verified)
				self.hidden_grid = self.gen_grid()
				self.set_mines(self.hidden_grid)
				# self.print_grid(self.hidden_grid)
			else:
				verified = True


		self.print_grid(self.hidden_grid)
		self.player_grid = self.gen_grid()
		time.sleep(self.displayInterval)

		# Re-arrange later to make interval more reliable
		self.posX = 0
		self.posY = 0
		self.player_grid[self.posX][self.posY] = self.playerChar
		self.print_grid(self.player_grid)



		while self.game_state() == "running":
			if msvcrt.kbhit():

				self.capture_input()

				if self.game_state() == "lose":
					for mines in self.minePos:
						x,y = mines
						self.player_grid[x][y]=self.mineChar
					# self.print_grid(self.player_grid)
					self.print_grid(self.player_grid)
					print("You stepped on a mine and set off all the others...")
					print("Would you like to Play Again?")
					print()
					break

				self.update_grid(self.player_grid)
				
				# if self.game_state() == "lose":
				# 	# self.print_grid(self.hidden_grid)

				# if self.game_state() == "win":
				# 	print("you win!")



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
