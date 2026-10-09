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
		self.image.fill((255, 0, 0))

	def input(self) -> None:
		keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
			
		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0
		if keys[pygame.K_a]:
			self.direction.x = -1
		elif keys[pygame.K_d]:
			self.direction.x = 1
		else:
			self.direction.x = 0

	def update(self, dt: float) -> None:
		self.input()
		return super().update(dt)
		