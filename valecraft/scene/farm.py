'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 18:50:25
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

from valecraft.display.camera import FarmCameraGroup
from valecraft.entities.player import Player

class Farm:
	def __init__(self) -> None:
		self.sprites_group: FarmCameraGroup = FarmCameraGroup()
		self.on_init()

	def on_init(self) -> None:
		self.player = Player((100, 100), self.sprites_group)

	def update(self, dt: float) -> None:
		self.player.update(dt)

	def draw(self) -> None:
		self.sprites_group.custom_draw(self.player)