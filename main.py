import itertools
import pandas
import numpy as np
from random import randint
class Game(object):

	def __init__(self):
		self.length = 10

	def gen_grid(self):
		grid = []
		thisRow = []
		for yCols in range(self.length):
			for xRows in range(self.length):
				thisRow.append(0)
			grid.append(thisRow)
			thisRow = []
		print(grid)
myGame = Game()
myGame.gen_grid()

# def print_array(array):
# 	for y in range(len(array)):
# 		for x in range(len(array)):
# 			print(array[x][y])

# # board = np.array([rows,cols])
# board = np.random.randint(1,100,(10,10))
# print(board)
# # print(' '.join(str(n) for n in board))
# print_array(board)