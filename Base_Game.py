import numpy as np
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, col, piece):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			board[r][col]=piece
			break

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def print_board(board):
	print(np.flip(board, 0))

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	for r in range(ROW_COUNT):
		for c in range(COLUMN_COUNT):
			if board[5-r][c] == 0:
				print('| |',end="")
			if board[5-r][c] == 1:
				print('|Y|',end="")
			if board[5-r][c] == 2:
				print('|R|',end="")
		print(" ")
	


#board = create_board()
#drop_piece(board,0,2)
#drop_piece(board,1,2)
#print(winning_move(board,2))
#draw_board(board)