import pygame, sys
from pygame import *
from math import sqrt

WINDOWWIDTH = 1280
WINDOWHEIGHT = 740
FPS = 30

ORANGE = (255, 168, 32)
BRIGHTRED = (255, 0 , 0)
BRIGHTGREEN = (64, 255, 64)
GREEN = (41, 191, 0)
RED = (223, 65, 0)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 64)
BROWN = (255, 215, 159)
BLUE = (96, 180, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BGCOLOR = BLUE
HIGHLIGHTCOLOR = ORANGE
BOARD = [[], [], [], [], [], [], [], [], []]

def main():
	global FPSCLOCK, DISPLAYSURF, BOARD
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption("Settlers of Catan")
	
	mousex = 0
	mousey = 0
	
	while True:
		mouseClicked = False
		DISPLAYSURF.fill(BGCOLOR)
		
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
def drawBoard():
	start = (561, 90)
	length = 80
	for hex in board[0]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (441, 160)
	for hex in board[1]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (321, 229)
	for hex in board[2]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (441, 299)
	for hex in board[3]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (321, 369)
	for hex in board[4]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (441, 439)
	for hex in board[5]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (321, 509)
	for hex in board[6]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (441, 579)
	for hex in board[7]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)
	start = (561, 647)
	for hex in board[8]:
		type = hex.resource
		number = hex.number
		start = drawHex(start, length, type, number)

def shuffleBoard():
	plots = [boardPiece(None, "Rock", None), boardPiece(None, "Rock", None), boardPiece(None, "Rock", None), boardPiece(None, "Wood", None), boardPiece(None, "Wood", None), boardPiece(None, "Wood", None), boardPiece(None, "Wood", None), boardPiece(None, "Brick", None), boardPiece(None, "Brick", None), boardPiece(None, "Brick", None), boardPiece(None, "Sheep", None), boardPiece(None, "Sheep", None), boardPiece(None, "Sheep", None), boardPiece(None, "Sheep", None), boardPiece(None, "Wheat", None), boardPiece(None, "Wheat", None), boardPiece(None, "Wheat", None), boardPiece(None, "Wheat", None), boardPiece(None, "Desert", None)]
	numbers = ["4", "11", "12", "6", "9", "3", "5", "8", "11", "10", "10", "4", "5", "9", "8", "2", "3", "6"]	
	random.shuffle(plots)
	random.shuffle(numbers)

	board[0].append(plots[0])
	board[1].append(plots[1])
	board[1].append(plots[2])
	board[2].append(plots[3])
	board[2].append(plots[4])
	board[2].append(plots[5])
	board[3].append(plots[6])
	board[3].append(plots[7])
	board[4].append(plots[8])
	board[4].append(plots[9])
	board[4].append(plots[10])
	board[5].append(plots[11])
	board[5].append(plots[12])
	board[6].append(plots[13])
	board[6].append(plots[14])
	board[6].append(plots[15])
	board[7].append(plots[16])
	board[7].append(plots[17])
	board[8].append(plots[18])
	for plot in plots:
		plot.location = plots.index(plot)
	for plot in plots:
		if plot.resource == "Desert":
			desert = plots.index(plot)
			del plots[desert]
	for plot in plots:
		plot.number = numbers.pop()
main()