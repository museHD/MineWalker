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
		self.nMines = 15
		self.displayInterval = 2
		self.path = []
		self.minePos = []
		self.scanChar = "*"
		self.powerups = 0
		self.score = 0


	# Restrict number to a min and max value to stop index error
	def restrict(self, n, low, high):
		if n < low:
			n += (low - n)
		if n > high:
			n -= (n - high)
		return n

	# Takes a 2D array, converts it to a pandas df and prints it to display
	def print_grid(self, grid):
		os.system("cls")
		print()

		df = pd.DataFrame(grid)
		print(df.to_string(index=False, header=False).replace(self.playerChar, color.GREEN + self.playerChar + color.BASE))

	# Does what print_grid does without using cls ~ Secret sauce to no flickering
	def update_grid(self, grid):

		# Moves cursor n number of lines up where n is the length of the grid
		print('\033[{0}A'.format(self.length+9))
		df = pd.DataFrame(grid)
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

	# Depht First Search algorithm
	def dfs(self, x = 0, y = 0):

		toVisit = self.toVisit
		self.hiddencopy = copy.copy(self.hidden_grid)
		self.hiddencopy = self.hidden_grid

		# Ensure that x and y don't cause indexErrors
		self.restrict(x,0,self.length-1)
		self.restrict(y,0,self.length-1)

		# Increment x and y to check them in the path
		nextX = x+1
		nextY = y+1

		self.restrict(nextX,0,self.length-1)
		self.restrict(nextY,0,self.length-1)


		right = (x,nextY)
		down = (nextX,y)
		up = (x-1,y)
		left = (x, y-1)

		# tuple vs list optimisation
		options = (right, down, up, left)

		# Go through all possible options for current coordinates
		for option in options:

			# If option is safe, then go to the option
			if option in toVisit:
				x,y = option

				# Remove from visit list to avoid repition
				toVisit.remove(option)

				# Check if path has been found
				if x == self.length-1 and y == self.length-1:
					return 0

				# Call dfs again to find next square in the path
				else:
					if self.dfs(x,y) == 0:
						return 0

		# If no path can be found:
		return 1

	# Calls above DFS to find path
	def verify_path(self):
		# hidden = copy.copy(self.hidden_grid)
		hidden = self.hidden_grid
		spotPath = []
		x = 0
		y = 0

		myPath = []
		
		# Create visit list containing every single square
		self.toVisit = []
		for x in range(self.length):
			for y in range(self.length):
				self.toVisit.append((x,y))


		# Remove mine positions from visit list
		# print(self.toVisit)
		for eachMine in self.minePos:
			if eachMine in self.toVisit:
				# print(eachMine)
				self.toVisit.remove(eachMine)

		# Run pathfinding algorithm
		if self.dfs() == 0:
			# print("YES")
			return True
		else:
			# print('no')
			return False

	# Function to calculate score
	def calculate_score(self):
		timeTaken = int(time.time() - self.startTime)
		score = 1000
		score = score * self.nMines^2
		score += self.length*1.5
		score -= timeTaken*1000
		score += self.powerups *15
		self.restrict(score,0,1000000000)
		self.score = score
		return score

	# Checks current game state using player position
	def game_state(self):

		state = "running"
		if self.hidden_grid[self.posX][self.posY] == self.mineChar:
			state = "lose"

			for mines in self.minePos:
				x,y = mines
				self.player_grid[x][y]=self.mineChar
			self.update_grid(self.player_grid)
			print("You stepped on a mine and set off all the others...")
			print()

		if self.posX == self.length-1 and self.posY == self.length-1:
			state = "win"
			print("You Win!")
			print()

		if state != "running":
			print(f"Your Score Was: {self.calculate_score()}")			
			# print("Would you like to Play Again?")
		return state


	# Move player after getting letter from capture input
	def move_player(self, direction):

		# IMPLEMENTING MOVELIST
		direction = direction.lower()
		moveList = {"d":(0,1), "a":(0,-1), "w":(-1,0), "s":(1,0)}
		poslist = [(0,1),(0,-1),(-1,0),(1,0)]

		# Keep powerups above 0
		self.restrict(self.powerups, 0, 10000000)

		# Move player if letter is in movelist
		if direction in moveList:
			self.player_grid[self.posX][self.posY] = self.pathChar
			addX, addY = moveList[direction]
			self.posX += addX
			self.posY += addY

			self.posX = self.restrict(self.posX,0,self.length-1)
			self.posY = self.restrict(self.posY,0,self.length-1)

			self.player_grid[self.posX][self.posY] = self.playerChar

		# Scan feature
		elif direction == "q":
			self.powerups -= 1
			if self.powerups > 1:
				print(f"Remaining Scans: {self.powerups}   \n")

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

				up = self.restrict(self.posY-1,0,self.length-1)
				down = self.restrict(self.posY+1,0,self.length-1)
				left = self.restrict(self.posX-1,0,self.length-1)
				right = self.restrict(self.posX+1,0,self.length-1)

				# print(up,down,left,right)
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

			else:
				print("No Remaining Powerups!        ")

		# Write player character
		self.player_grid[self.posX][self.posY] = self.playerChar

	# Capture single key input from stack
	def capture_input(self): 

		key_stroke = msvcrt.getch()

		# If Special character: map each arrow key to wasd
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

		# Convert to unicode to make life easier
		try:
			key_stroke = (str(key_stroke, 'utf-8'))
			self.move_player(key_stroke)
		except UnicodeDecodeError:
			pass

	def run(self):

		self.startTime = time.time()

		self.path = []
		self.minePos = []
		run = True

		self.hidden_grid = self.gen_grid()
		self.set_mines(self.hidden_grid)

		# Verify path, if it fails, keep generating grids till verified
		verified = False
		while verified == False:
			if self.verify_path() == False:
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


		# Main game loop that captures input and updates grid according to that
		while self.game_state() == "running":
			if msvcrt.kbhit():
				self.capture_input()
				self.update_grid(self.player_grid)
		
