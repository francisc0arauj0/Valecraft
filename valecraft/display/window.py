'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 17:56:10
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

class GameWindow:
	def __init__(self, name: str) -> None:
		self.name = name
		self.window_size = (800, 600)
		self.display = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
		self.fullscreen = False

	def toggle_fullscreen(self) -> None:
		self.fullscreen = not self.fullscreen

		if self.fullscreen:
			self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		else:
			self.display = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN)

	def resize(self, size: tuple[int, int]) -> None:
		if not self.fullscreen:
			self.window_size = size
			self.display = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

