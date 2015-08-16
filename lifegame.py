# -*- coding: utf-8 -*-

try:
	import pygame
	import random
	import os
	from pygame.locals import *
except ImportError:
	raise SystemError('Module not found')
	
class Config:
	sizewindow = 500, 500
	sizepoint  = 5, 5
	
def terminate():
	pygame.quit()
	os.sys.exit(0)

def eventmanager():
	for event in pygame.event.get():
		if event.type == QUIT:
			terminate()

class Board:
	def __init__(self):
		self.lcell = set()
		
	def neighbors(self, x, y):
		return (
				(x + 1, y), (x, y + 1), 
				(x - 1, y), (x, y - 1),
				(x + 1, y + 1), 
				(x - 1, y - 1), 
				(x + 1, y - 1),
				(x - 1, y + 1)
				)

	def wakeup(self, x, y):
		self.lcell.add((x, y))
			
	def update(self):
		bagcell = {}
		tmp = set()
		for livec in self.lcell:
			for n in self.neighbors(*livec):
				if n not in bagcell:
					bagcell[n] = 1
				else:
					bagcell[n] += 1
		for cell, adds in bagcell.items():
			if((adds == 2 or adds == 3) and cell in self.lcell) or (adds == 3 and cell not in self.lcell):
				tmp.add(cell)
		self.lcell = tmp

	def draw(self, surface, surface_):
		surface.blit(surface_, (0, 0))
		for cell in self.lcell:
			x, y   = cell
			x_, y_ = Config.sizepoint
			pygame.draw.rect(surface, (255, 255, 255), ((x * 5, y * 5), (5, 5)), 1)
			
	def fill(self, n):
		edgex = Config.sizewindow[0] // Config.sizepoint[0]
		edgey = Config.sizewindow[1] // Config.sizepoint[1]
		while n > len(self.lcell):
			self.wakeup(random.randint(0, edgex), random.randint(0, edgey))

def main():
	main_clock = pygame.time.Clock()
	pygame.display.init()
	window  = pygame.display.set_mode(Config.sizewindow)
	pygame.display.set_caption('Game of Life')
	window_ = window.copy()
	board  = Board()
	board.fill(5000)
	while 1:
		eventmanager()
		board.draw(window, window_)
		board.update()
		pygame.display.flip()
		main_clock.tick(5)


main()
