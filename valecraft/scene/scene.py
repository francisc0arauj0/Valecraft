'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 18:50:25
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

from __future__ import annotations

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING: from valecraft.game import Game
from valecraft.entities.player import Player

class Scene:
	def __init__(self, game: Game, map_name: str) -> None:
		self.game = game
		self.map_name = map_name
		self.sprites_group: pygame.sprite.Group[pygame.sprite.Sprite] = pygame.sprite.Group()

		self.on_init()

	def on_init(self) -> None:
		self.player = Player(position=(100, 100), group=self.sprites_group)

	def update(self, dt: float) -> None:
		self.player.update(dt=dt)

	def draw(self, window: pygame.Surface) -> None:
		self.sprites_group.draw(surface=window)