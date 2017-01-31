import pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1080
WINDOWHEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BGCOLOR = BLACK

def main():
	global FPS, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	
	mousex = 0
	mousey = 0
	pygame.display.set_caption("Board Games")
	DISPLAYSURF.fill(BGCOLOR)
	
	while True:
		mouseClicked = False
		
		DISPLAYSURF.fill(BGCOLOR)
		
		drawbuttons()
		for event in pygame.event.get():
			if event.type == QUIT  or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
		if (mousex, mousey) == collide
		
				
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
def drawbuttons():
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj1 = fontObj.render('Board Games', True, GREEN, BLACK)
	textRectObj1 = textSurfaceObj1.get_rect()
	textRectObj1.center = (540, 50)
	DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
	
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj2 = fontObj.render('Chess', True, GREEN, BLUE)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center = (540, 350)
	DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
	
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj3 = fontObj.render('Checkers', True, GREEN, BLUE)
	textRectObj3 = textSurfaceObj3.get_rect()
	textRectObj3.center = (540, 450)
	DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)
main()