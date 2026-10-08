'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 00:46:23
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

class SceneManager:
	def __init__(self, game) -> None:
		self.game = game
		self.current_scene = None

	def change(self, scene) -> None:
		self.current_scene = scene

	def events(self, events: list[pygame.event.Event]) -> None:
		if self.current_scene:
			self.current_scene.events(events)

	def update(self, dt: float) -> None:
		if self.current_scene:
			self.current_scene.update(dt)

	def draw(self, screen: pygame.Surface) -> None:
		if self.current_scene:
			self.current_scene.draw(screen)