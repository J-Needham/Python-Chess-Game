import pygame, sys
from pygame import *

WINDOWWIDTH = 500
WINDOWHEIGHT = 500
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (255, 255, 255)

class Screen(object):
		
	def open(self):
		pass
		
class Engine(object):
	def __init__(self, display):
		self.display = display
		
		
	def run(self):
		DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
		pygame.display.set_caption("Drawing")
		pygame.init()
		current_screen = self.display.opening_screen()
		while True:
			DISPLAYSURF.fill(WHITE)
			current_screen.open()
			COLOR = current_screen.color
			pygame.draw.rect(DISPLAYSURF, COLOR, (200, 50, 100, 50))
			
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == KEYUP and event.key == K_g:
					name = current_screen.next_screen_name
					current_screen = self.display.next_screen(name)
			pygame.display.update()
			
class OpeningScreen(Screen):
	def open(self):	
		self.name = "Opening Screen"
		self.color = RED
		self.next_screen_name = "screen1"
	
class ScreenOne(Screen):
	def open(self):
		self.name = "Screen One"
		self.color = BLUE
		self.next_screen_name = "screen2"
	
class ScreenTwo(Screen):
	def open(self):
		self.name = "Screen Two"
		self.color = GREEN
		self.next_screen_name = "screen3"
	
class ScreenThree(Screen):
	def open(self):
		self.name = "Screen Three"
		self.color = YELLOW
		self.next_screen_name = "closing screen"
	
class ClosingScreen(Screen):
	def open(self):
		self.name = "Closing Screen"
		self.color = BLACK
		self.next_screen_name = pygame.quit(), sys.exit()
					
	
		
	
class Display(object):
	
	screens = {
		"opening screen" : OpeningScreen(),
		"screen1" : ScreenOne(),
		"screen2" : ScreenTwo(),
		"screen3" : ScreenThree(),
		"closing screen" : ClosingScreen(),
	}
	
	def __init__(self, start_screen):
		self.start_screen = start_screen
		
	def opening_screen(self):
		return self.next_screen(self.start_screen)
		
	def next_screen(self, next_screen_name):
		val = self.screens.get(next_screen_name)
		return val

a_display = Display("opening screen")
a_game = Engine(a_display)
a_game.run()