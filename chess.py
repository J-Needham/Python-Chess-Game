import pygame, sys, itertools
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1080
WINDOWHEIGHT = 720
BOXSIZE = 80
BOARDWIDTH = 8
BOARDHEIGHT = 8
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * BOXSIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE)) / 2)

GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
ORANGE = (255, 154, 32)
LIGHTBLUE = (0, 175, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
PURPLE = (255, 0, 239)
YELLOW = (247, 255, 0)
BROWN = (191, 99, 0)

BGCOLOR = GRAY
HIGHLIGHTCOLOR = BLUE
PLAYER1COLOR = ORANGE
PLAYER2COLOR = LIGHTBLUE
def main():
	global FPSCLOCK, DISPLAYSURF, turn
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	
	mousex = 0
	mousey = 0
	pygame.display.set_caption('Chess')
	
	DISPLAYSURF.fill(BGCOLOR)
	firstSelection = None
	secondSelection = None
	turn = []
	while True:
		mouseClicked = False
		
		DISPLAYSURF.fill(BGCOLOR)
		drawBoard()
		drawPieces()
		playerturn = getPlayer(turn)
		drawPlayerScreen(playerturn)
		for event in pygame.event.get():
			if event.type == QUIT  or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
	
		boxx, boxy = getBoxAtPixel(mousex, mousey)
		
		if firstSelection != None:
			x, y = firstSelection
			highlight(x, y)
			currentpiece = getpiece(x, y)
		
		if boxx != None and boxy != None:
			highlight(boxx, boxy)
			if mouseClicked == True and firstSelection == None:
				firstSelection = boxx, boxy
			elif mouseClicked == True and firstSelection != None:
				secondSelection = boxx, boxy
				if currentpiece != None:
					collide, capture = checkcollide(firstSelection, secondSelection, currentpiece)
					currentpiece.move(firstSelection, secondSelection, currentpiece, collide, playerturn, capture)
					
					firstSelection = None
					secondSelection = None
					collide = None
					capture = None
				else:
					firstSelection = None
					secondSelection = None
				
				
				
				
				
		pygame.display.update()
		FPSCLOCK.tick(FPS)

			
			
	
				
def drawPlayerScreen(player):
	if player == "Player1":
		fontObj = pygame.font.Font('freesansbold.ttf', 32)
		textSurfaceObj = fontObj.render('Player One Move', True, WHITE, BLACK)
		textRectObj = textSurfaceObj.get_rect()
	
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	elif player == "Player2":
		fontObj = pygame.font.Font('freesansbold.ttf', 32)
		textSurfaceObj = fontObj.render('Player Two Move', True, WHITE, BLACK)
		textRectObj = textSurfaceObj.get_rect()
		
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
def getPlayer(turn):
	i = len(turn)
	if i % 2 == 1:
		return "Player2"
	else:
		return "Player1"
		
def getBoxAtPixel(x, y):
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left, top = leftTopCoordsOfBox(boxx, boxy)
			boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
			if boxRect.collidepoint(x, y):
				return (boxx, boxy)
	return (None, None)
	
def getpiece(boxx, boxy):
	for piece in player1pieces:
		if piece.location == (boxx, boxy):
			return piece
		
		for piece in player2pieces:
			if piece.location == (boxx, boxy):
				return piece
			
			
						
def leftTopCoordsOfBox(boxx, boxy):
	left = boxx * BOXSIZE + XMARGIN
	top = boxy * BOXSIZE + YMARGIN
	return (left, top)
	
def drawBoard():
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			if x % 2 == 0:
				if y % 2 ==0:
					pygame.draw.rect(DISPLAYSURF, BLACK, ((XMARGIN+(x*BOXSIZE)), (YMARGIN+(y*BOXSIZE)), BOXSIZE, BOXSIZE),0)
				else:
					pygame.draw.rect(DISPLAYSURF, WHITE, ((XMARGIN+(x*BOXSIZE)), (YMARGIN+(y*BOXSIZE)), BOXSIZE, BOXSIZE),0)
			else:
				if y % 2 ==1:
					pygame.draw.rect(DISPLAYSURF, BLACK, ((XMARGIN+(x*BOXSIZE)), (YMARGIN+(y*BOXSIZE)), BOXSIZE, BOXSIZE),0)
				else:
					pygame.draw.rect(DISPLAYSURF, WHITE, ((XMARGIN+(x*BOXSIZE)), (YMARGIN+(y*BOXSIZE)), BOXSIZE, BOXSIZE),0)

def highlight(boxx, boxy):
	left, top = leftTopCoordsOfBox(boxx, boxy)
	pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

def drawPieces():
	for piece in player1pieces:
		x, y = piece.location
		if x % 2 == 0:
			if y % 2 == 0:
				color = "black"
			else:
				color = "white"
		else:
			if y % 2 == 1:
				color = "black"
			else: 
				color = "white"
		
		
		if piece.type == "Pawn":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('pawn1black.bmp')
			else:
				picture = pygame.image.load('pawn1.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Castle":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('castle1black.bmp')
			else:
				picture = pygame.image.load('castle1.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Bishop":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('bishop1black.bmp')
			else:
				picture = pygame.image.load('bishop1.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Queen":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('queen1black.bmp')
			else:
				picture = pygame.image.load('queen1.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "King":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('king1black.bmp')
			else:
				picture = pygame.image.load('king1.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Knight":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('knight1black.bmp')
			else:
				picture = pygame.image.load('knight1.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
	for piece in player2pieces:
		x, y = piece.location
		if x % 2 == 0:
			if y % 2 == 1:
				color = "white"
			else:
				color = "black"
		else:
			if y % 2 == 1:
				color = "black"
			else: 
				color = "white"
		
				
		if piece.type == "Pawn":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('pawn2black.bmp')
			else:
				picture = pygame.image.load('pawn2.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Castle":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('castle2black.bmp')
			else:
				picture = pygame.image.load('castle2.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Bishop":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('bishop2black.bmp')
			else:
				picture = pygame.image.load('bishop2.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Queen":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('queen2black.bmp')
			else:
				picture = pygame.image.load('queen2.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "King":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('king2black.bmp')
			else:
				picture = pygame.image.load('king2.bmp')
			DISPLAYSURF.blit(picture, (left, top))
			
		elif piece.type == "Knight":
			boxx, boxy = piece.location
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if color == "black":
				picture = pygame.image.load('knight2black.bmp')
			else:
				picture = pygame.image.load('knight2.bmp')
			DISPLAYSURF.blit(picture, (left, top))

			
def checkcollide(firstSelection, secondSelection, currentpiece):
	capture = None
	tick = []
	fx, fy = firstSelection
	sx, sy = secondSelection
	
	for obstacle in player1pieces:
		ox, oy = obstacle.location
		
		if secondSelection == obstacle.location:
				if currentpiece.player == obstacle.player:
					tick.append("1")
				elif currentpiece.player != obstacle.player:
					tick.append("1")
					capture = player1pieces.index(obstacle)
				
		
		elif currentpiece.type == "Castle":
			if ox > fx and ox < sx and oy == sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy == sy:
				tick.append("1")
			elif oy > fy and oy < sy and ox == sx:
				tick.append("1")
			elif oy < fy and oy > sy and ox == sx:
				tick.append("1")
			
		elif currentpiece.type == "Queen":
			if ox > fx and ox < sx and oy == sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy == sy:
				tick.append("1")
			elif oy > fy and oy < sy and ox == sx:
				tick.append("1")
			elif oy < fy and oy > sy and ox == sx:
				tick.append("1")
			elif ox > fx and ox < sx and oy > fy and oy < sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy < fy and oy > sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy > fy and oy < sy:
				tick.append("1")
			elif ox > fx and ox < sx and oy < fy and oy > sy:
				tick.append("1")
		#elif currentpiece.type == "Knight" and secondSelection != obstacle.location:
			#return False, capture	
		
		elif currentpiece.type == "Bishop":
			route = []
			for i in range(abs(fx - sx)):
				if fx - sx < 0 and fy - sy > 0:
					x = fx =+ 1
					y = fy =- 1
					route.append((x, y))
				elif fx - sx < 0 and fy - sy < 0:
					x = fx =+ 1
					y = fy =+ 1
					route.append((x, y))
				elif fx - sx > 0 and fy - sy > 0:
					x = fx =- 1
					y = fy =- 1
					route.append((x, y))
				elif fx - sx > 0 and fy - sy < 0:
					x = fx =- 1
					y = fy =+ 1
					route.append((x, y))
						
				if (ox, oy) in route:
					tick.append("1")
					
		elif currentpiece.type == "Pawn":
			if oy > fy and oy < sy and ox == fx:
				tick.append("1")
			
		
	for obstacle in player2pieces:
		ox, oy = obstacle.location
		
		if secondSelection == obstacle.location:
				if currentpiece.player == obstacle.player:
					tick.append("1")
				elif currentpiece.player != obstacle.player:
					tick.append("1")
					capture = player2pieces.index(obstacle)
				
				
		
		elif currentpiece.type == "Castle":
			if ox > fx and ox < sx and oy == sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy == sy:
				tick.append("1")
			elif oy > fy and oy < sy and ox == sx:
				tick.append("1")
			elif oy < fy and oy > sy and ox == sx:
				tick.append("1")
			
		elif currentpiece.type == "Queen":
			if ox > fx and ox < sx and oy == sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy == sy:
				tick.append("1")
			elif oy > fy and oy < sy and ox == sx:
				tick.append("1")
			elif oy < fy and oy > sy and ox == sx:
				tick.append("1")
			elif ox > fx and ox < sx and oy > fy and oy < sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy < fy and oy > sy:
				tick.append("1")
			elif ox < fx and ox > sx and oy > fy and oy < sy:
				tick.append("1")
			elif ox > fx and ox < sx and oy < fy and oy > sy:
				tick.append("1")
		#elif currentpiece.type == "Knight" and secondSelection != obstacle.location:
			#return False, capture
		
		elif currentpiece.type == "Bishop":
			route = []
			for i in range(abs(fx - sx)):
				if fx - sx < 0 and fy - sy > 0:
					x = fx =+ 1
					y = fy =- 1
					route.append((x, y))
				elif fx - sx < 0 and fy - sy < 0:
					x = fx =+ 1
					y = fy =+ 1
					route.append((x, y))
				elif fx - sx > 0 and fy - sy > 0:
					x = fx =- 1
					y = fy =- 1
					route.append((x, y))
				elif fx - sx > 0 and fy - sy < 0:
					x = fx =- 1
					y = fy =+ 1
					route.append((x, y))
						
				if (ox, oy) in route:
					tick.append("1")
			
				
				
			
			
		elif currentpiece.type == "Pawn":
			if oy < fy and oy > sy and ox == fx:
				tick.append("1")
				
	if currentpiece.type == "Queen" and tick.count("1") > 1:
		return True, capture
	elif currentpiece.type == "Queen" and tick.count("1") == 1:
		return "attack" , capture
		
	
	
	
			
	if "1" in tick:
		return True, capture
	else:
		return False, capture
		

class piece(object):
	
	def __init__(self, name, type, player, location):
		self.player = player
		self.location = location
		self.type = type
		self.start = location
		
	
	
class pawn(piece):

	def move(self, firstSelection, secondSelection, currentpiece, collide, playerturn, capture):
		fx, fy = firstSelection
		sx, sy = secondSelection
		playerpiece = currentpiece.player
		if playerturn == "Player1":
			if playerpiece == "Player1":
				if firstSelection == currentpiece.start and sx == fx and sy == (fy + 2) and collide == False:
					currentpiece.location = secondSelection 
					turn.append('1')
				elif sy == (fy + 1) and sx == fx and collide == False:
					currentpiece.location = secondSelection
					turn.append('1')
				elif fx - 1 == sx and fy + 1 == sy and capture != None:
					currentpiece.location = secondSelection
					turn.append('1')
					del player2pieces[capture]
				elif fx + 1 == sx and fy + 1 == sy and capture != None:
					currentpiece.location = secondSelection
					turn.append('1')
					del player2pieces[capture]
		elif playerturn == "Player2":
			if playerpiece == "Player2":
				if firstSelection == currentpiece.start and sx == fx and sy == (fy - 2) and collide == False:
					currentpiece.location = secondSelection
					turn.append('1')
				elif sy == (fy - 1) and sx == fx and collide == False:
					currentpiece.location = secondSelection
					turn.append('1')
				elif fx - 1 == sx and fy - 1 == sy and capture != None:
					currentpiece.location = secondSelection
					turn.append('1')
					del player1pieces[capture]
				elif fx + 1 == sx and fy - 1 == sy and capture != None:
					currentpiece.location = secondSelection
					turn.append('1')
					del player1pieces[capture]
	
	def attack(self):
		pass

class castle(piece):
	
	def move(self, firstSelection, secondSelection, currentpiece, collide, playerturn, capture):
		fx, fy = firstSelection
		sx, sy = secondSelection
		player = currentpiece.player
		list = None
		if player == "Player1":
			list = player2pieces
		elif player == "Player2":
			list = player1pieces
		
		if player == playerturn:
			if (sx == fx or fy == sy) and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif (sx == fx or fy == sy) and capture != None:
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
				
		
		
	def attack(self):
		
		pass

class knight(piece):

	def move(self, firstSelection, secondSelection, currentpiece, collide, playerturn, capture):
		fx, fy = firstSelection
		sx, sy = secondSelection
		player = currentpiece.player
		list = None
		
		if player == "Player1":
			list = player2pieces
		elif player == "Player2":
			list = player1pieces
		
		if player == playerturn:
			if abs(fx - sx) == 1 and abs(fy - sy) == 2 and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif abs(fx - sx) == 2 and abs(fy - sy) == 1 and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif abs(fx - sx) == 1 and abs(fy - sy) == 2 and capture != None:
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
			elif abs(fx - sx) == 2 and abs(fy - sy) == 1 and capture != None:
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
				
	
	def attack(self):
		pass

class bishop(piece):
	
	def move(self, firstSelection, secondSelection, currentpiece, collide, playerturn, capture):
		fx, fy = firstSelection
		sx, sy = secondSelection
		player = currentpiece.player
		list = None
		
		if player == "Player1":
			list = player2pieces
		elif player == "Player2":
			list = player1pieces
		
		if player == playerturn:
			if (fx != sx) and (fy != sy) and (abs(fx - sx) == abs(fy - sy)) and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif (fx != sx) and (fy != sy) and (abs(fx - sx) == abs(fy - sy)) and capture != None:
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
	
	def attack(self):
		pass

class king(piece):
	
	def move(self, firstSelection, secondSelection, currentpiece, collide, playerturn, capture):
		fx, fy = firstSelection
		sx, sy = secondSelection
		player = currentpiece.player
		list = None
		
		if player == "Player1":
			list = player2pieces
		elif player == "Player2":
			list = player1pieces
		
		if player == playerturn:
			if (abs(fx - sx) == abs(fy - sy)) and (abs(fx - sx) == 1 or abs(fy - sy) == 1) and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif (sx == fx or fy == sy) and (abs(fx - sx) == 1 or abs(fy - sy) == 1) and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif (abs(fx - sx) == abs(fy - sy)) and (abs(fx - sx) == 1 or abs(fy - sy) == 1) and capture != None:
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
			elif (sx == fx or fy == sy) and (abs(fx - sx) == 1 or abs(fy - sy) == 1) and capture != None:
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
			
		
		
	def attack(self):
		pass

class queen(piece):
	
	def move(self, firstSelection, secondSelection, currentpiece, collide, playerturn, capture):
		fx, fy = firstSelection
		sx, sy = secondSelection
		player = currentpiece.player
		list = None
		
		if player == "Player1":
			list = player2pieces
		elif player == "Player2":
			list = player1pieces
		
		if player == playerturn:
			if (fx != sx) and (fy != sy) and (abs(fx - sx) == abs(fy - sy)) and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif (sx == fx or fy == sy) and collide == False:
				currentpiece.location = secondSelection
				turn.append('1')
			elif (fx != sx) and (fy != sy) and (abs(fx - sx) == abs(fy - sy)) and capture != None and collide == "attack":
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
			elif (sx == fx or fy == sy) and capture != None and collide == "attack":
				currentpiece.location = secondSelection
				turn.append('1')
				del list[capture]
			
		
		
	def attack(self):
		pass
			
player1pieces = [pawn("Pawn 1","Pawn", "Player1", (0,1)), pawn("Pawn 2", "Pawn", "Player1", (1,1)), pawn("Pawn 3", "Pawn", "Player1", (2,1)), pawn("Pawn 4", "Pawn", "Player1", (3,1)), pawn("Pawn 5", "Pawn", "Player1", (4,1)), pawn("Pawn 6", "Pawn", "Player1", (5,1)), pawn("Pawn 7", "Pawn", "Player1", (6,1)), pawn("Pawn 8", "Pawn", "Player1", (7,1)), castle("Castle 1", "Castle", "Player1", (0,0)), castle("Castle 2", "Castle", "Player1", (7,0)), bishop("Bishop 1", "Bishop", "Player1", (2,0)), bishop("Bishop 2", "Bishop", "Player1", (5,0)), queen("Queen 1", "Queen", "Player1", (3,0)), king("King 1", "King", "Player1", (4,0)), knight("Knight 1", "Knight", "Player1", (1,0)), knight("Knight 2", "Knight", "Player1", (6,0))]
player2pieces = [pawn("Pawn 1","Pawn", "Player2", (0,6)), pawn("Pawn 2", "Pawn", "Player2", (1,6)), pawn("Pawn 4", "Pawn", "Player2", (2,6)), pawn("Pawn 4", "Pawn", "Player2", (3,6)), pawn("Pawn 5", "Pawn", "Player2", (4,6)), pawn("Pawn 6", "Pawn", "Player2", (5,6)), pawn("Pawn 7", "Pawn", "Player2", (6,6)), pawn("Pawn 8", "Pawn", "Player2", (7,6)), castle("Castle 1", "Castle", "Player2", (0,7)), castle("Castle 2", "Castle", "Player2", (7,7)), bishop("Bishop 1", "Bishop", "Player2", (2,7)), bishop("Bishop 2", "Bishop", "Player2", (5,7)), queen("Queen 1", "Queen", "Player2", (4,7)), king("King 1", "King", "Player2", (3,7)), knight("Knight 1", "Knight", "Player2", (1,7)), knight("Knight 2", "Knight", "Player2", (6,7))]
main()

			#if ox > fx and ox < sx and oy > fy and oy < sy:
				#tick.append("1")
			#elif ox < fx and ox > sx and oy != fy and oy < fy and oy > sy:
				#tick.append("1")
			#elif ox < fx and ox > sx and oy != fy and oy > fy and oy < sy:
				#tick.append("1")
			#elif ox > fx and ox < sx and oy < fy and oy > sy:
				#tick.append("1")
			