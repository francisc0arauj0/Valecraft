'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 14:15:52
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame
import sys

class Game:
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Valecraft")
		self.clock = pygame.time.Clock()
		self.dt = 0
		self.time = 0
		self.is_running = True

	def update(self) -> None:
		self.dt = self.clock.tick() / 1000
		self.time = pygame.time.get_ticks()
		pygame.display.update()

	def events(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.is_running = False

	def run(self) -> None:
		while self.is_running:
			self.events()
			self.update()
		pygame.quit()
		sys.exit()

	