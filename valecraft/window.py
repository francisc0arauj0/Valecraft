'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 17:56:10
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

class GameWindow:
	def __init__(self, name: str) -> None:
		self.name: str = name

		self.window_size: tuple[int , int] = (800, 600)
		self.surface: pygame.Surface = pygame.display.set_mode(size=self.window_size, flags=pygame.RESIZABLE)
		
		self.fullscreen: bool = False

	def toggle_fullscreen(self) -> None:
		self.fullscreen = not self.fullscreen

		if self.fullscreen:
			self.surface = pygame.display.set_mode(size=(0,0), flags=pygame.FULLSCREEN)
		else:
			self.surface = pygame.display.set_mode(size=self.window_size, flags=pygame.FULLSCREEN)

	def resize(self, size: tuple[int, int]) -> None:
		if not self.fullscreen:
			self.window_size = size
			self.surface = pygame.display.set_mode(size=self.window_size, flags=pygame.RESIZABLE)

