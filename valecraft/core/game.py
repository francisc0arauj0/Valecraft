'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 14:15:52
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame
import sys

from valecraft.core.display import Display

class Game:
	def __init__(self) -> None:
		pygame.init()

		self.display = Display()

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
			if event.type == pygame.VIDEORESIZE:
				self.display.resize((event.w, event.h))
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					self.display.toggle_fullscreen()

	def run(self) -> None:
		while self.is_running:
			self.events()
			self.update()
		pygame.quit()
		sys.exit()

	