'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 02:14:52
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

from valecraft.entities.entity import Entity

class Player(Entity):
	def __init__(self, position: tuple[float, float], group: pygame.sprite.Group[pygame.sprite.Sprite]) -> None:
		super().__init__(position, group)
		self.speed = 100
		self.is_player = True