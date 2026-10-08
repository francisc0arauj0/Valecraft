'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 14:15:52
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import sys
import pygame

from valecraft.scene.manager import SceneManager
from valecraft.window import GameWindow

class Game:
	def __init__(self) -> None:
		pygame.init()

		self.window: GameWindow = GameWindow(name="Valecraft")

		self.clock: pygame.Clock = pygame.time.Clock()
		self.dt: float = 0.0
		self.time: int = 0
		
		self.is_running: bool = True
		self.on_init()

	def on_init(self) -> None:
		self.scene_manager = SceneManager(game=self)

	def events(self) -> None:
		events: list[pygame.Event] = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT:
				self.is_running = False
			if event.type == pygame.VIDEORESIZE:
				self.window.resize(size=(event.w, event.h))
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					self.window.toggle_fullscreen()

	def update(self) -> None:
		self.dt = self.clock.tick() / 1000
		self.time = pygame.time.get_ticks()

		self.scene_manager.update(dt=self.dt)

	def draw(self) -> None:
		self.window.surface.fill(color=(0, 0, 0))
		self.scene_manager.draw(window=self.window.surface)
		pygame.display.update()
		
	def run(self) -> None:
		while self.is_running:
			self.events()
			self.update()
			self.draw()
		pygame.quit()
		sys.exit()