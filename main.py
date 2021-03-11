import itertools
import pandas
import numpy as np
from random import randint

class Game(object):

	def __init__(self):
		self.length = 10

	# Takes a 2D array, converts it to a pandas df and prints it to display
	# TODO: Find out if the entire grid can be reprinted in console
	def print_grid(self, grid):
		df = pandas.DataFrame(grid)
		print(df.to_string(index=False, header=False))

	# Generates a simple 2d array
	def gen_grid(self):

		grid = []
		thisRow = []
		# Box unicode 
		boxChar = "\u2610"

		# Populates a 2D array with box characters
		for yCols in range(self.length):
			for xRows in range(self.length):
				thisRow.append(boxChar)
			grid.append(thisRow)
			thisRow = []
		return grid


myGame = Game()
myGame.gen_grid()


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