'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 18:17:00
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self, position: tuple[float, float], group: pygame.sprite.Group[pygame.sprite.Sprite]) -> None:
		super().__init__(group)

		self.direction = pygame.Vector2()
		self.speed = 0

		self.image: pygame.Surface = pygame.Surface(size=(24, 32))
		self.rect: pygame.Rect = self.image.get_rect(center=position)
		self.position = pygame.Vector2(self.rect.center)

	def move(self, dt: float) -> None:
		# Normalize
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# Horizontal
		self.position.x += self.direction.x * self.speed * dt
		self.rect.centerx = self.position.x

		# Vertical
		self.position.y += self.direction.y * self.speed * dt
		self.rect.centery = self.position.y

	def update(self, dt: float) -> None:
		self.move(dt=dt)