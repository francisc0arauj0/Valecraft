'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 00:46:23
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

from __future__ import annotations

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING: from valecraft.game import Game
from valecraft.scene.scene import Scene


class SceneManager:
	def __init__(self, game: Game) -> None:
		self.game = game
		self.current_scene = Scene(game=self.game, map_name="Farm")

	def change(self, scene: Scene) -> None:
		self.current_scene = scene

	def update(self, dt: float) -> None:
		self.current_scene.update(dt=dt)

	def draw(self, window: pygame.Surface) -> None:
		self.current_scene.draw(window=window)