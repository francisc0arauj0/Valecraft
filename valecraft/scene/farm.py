'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 18:50:25
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

from valecraft.display.camera import CameraGroup
from valecraft.entities.player import Player

class Farm:
	def __init__(self) -> None:
		self.camera_group: CameraGroup = CameraGroup()
		self.on_init()

	def on_init(self) -> None:
		self.player = Player((100, 100), self.camera_group)

	def events(self, event: pygame.Event) -> None:
		if event.type == pygame.VIDEORESIZE:
			self.camera_group.resize(event.size)

	def update(self, dt: float) -> None:
		self.camera_group.update(dt)
		self.player.update(dt)

	def draw(self) -> None:
		self.camera_group.custom_draw(self.player)