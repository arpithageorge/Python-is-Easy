import numpy as np
import pygame
import sys
import math

blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

row_count = 6
column_count = 7

def create_board():
	board = np.zeros((row_count,column_count))
	return board

def drop_color_coin(board, row, col, coin):
	board[row][col] = coin

def is_valid_location(board, col):
	return board[row_count-1][col] == 0

def get_next_open_row(board, col):
	for r in range(row_count):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

def winning_move(board, coin):
	# Check horizontal locations for win
	for c in range(column_count-3):
		for r in range(row_count):
			if board[r][c] == coin and board[r][c+1] == coin and board[r][c+2] == coin and board[r][c+3] == coin:
				return True

	# Check vertical locations for win
	for c in range(column_count):
		for r in range(row_count-3):
			if board[r][c] == coin and board[r+1][c] == coin and board[r+2][c] == coin and board[r+3][c] == coin:
				return True

	# Check positively sloped diaganols
	for c in range(column_count-3):
		for r in range(row_count-3):
			if board[r][c] == coin and board[r+1][c+1] == coin and board[r+2][c+2] == coin and board[r+3][c+3] == coin:
				return True

	# Check negatively sloped diaganols
	for c in range(column_count-3):
		for r in range(3, row_count):
			if board[r][c] == coin and board[r-1][c+1] == coin and board[r-2][c+2] == coin and board[r-3][c+3] == coin:
				return True

def draw_board(board):
	for c in range(column_count):
		for r in range(row_count):
			pygame.draw.rect(screen, blue, (c*BOXSIZE, r*BOXSIZE+BOXSIZE, BOXSIZE, BOXSIZE))
			pygame.draw.circle(screen, black, (int(c*BOXSIZE+BOXSIZE/2), int(r*BOXSIZE+BOXSIZE+BOXSIZE/2)), RADIUS)
	
	for c in range(column_count):
		for r in range(row_count):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, red, (int(c*BOXSIZE+BOXSIZE/2), height-int(r*BOXSIZE+BOXSIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, yellow, (int(c*BOXSIZE+BOXSIZE/2), height-int(r*BOXSIZE+BOXSIZE/2)), RADIUS)
	pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

BOXSIZE = 100

width = column_count * BOXSIZE
height = (row_count+1) * BOXSIZE

size = (width, height)

RADIUS = int(BOXSIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, black, (0,0, width, BOXSIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, red, (posx, int(BOXSIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, yellow, (posx, int(BOXSIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, black, (0,0, width, BOXSIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/BOXSIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_color_coin(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Player 1 wins!!", 1, red)
						screen.blit(label, (40,10))
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/BOXSIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_color_coin(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 wins!!", 1, yellow)
						screen.blit(label, (40,10))
						game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

			if game_over:
				pygame.time.wait(3000)
