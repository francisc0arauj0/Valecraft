'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 14:15:52
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame
import sys

from valecraft.core.display import Display
from valecraft.scene.level import Level
from valecraft.scene.manager import SceneManager

class Game:
	def __init__(self) -> None:
		pygame.init()
		self.display = Display()
		self.clock = pygame.time.Clock()
		self.dt = 0
		self.time = 0
		self.is_running = True
		self.on_init()

	def on_init(self) -> None:
		self.scene_manager = SceneManager(self)
		self.scene_manager.change(Level(self, "Farm"))

	def update(self) -> None:
		self.dt = self.clock.tick() / 1000
		self.time = pygame.time.get_ticks()
		self.scene_manager.update(self.dt)

	def draw(self) -> None:
		self.display.screen.fill((0, 0, 0))
		self.scene_manager.draw(self.display.screen)
		pygame.display.update()

	def events(self) -> None:
		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT:
				self.is_running = False
			if event.type == pygame.VIDEORESIZE:
				self.display.resize((event.w, event.h))
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					self.display.toggle_fullscreen()
		
		self.scene_manager.events(events)

	def run(self) -> None:
		while self.is_running:
			self.events()
			self.update()
			self.draw()
		pygame.quit()
		sys.exit()