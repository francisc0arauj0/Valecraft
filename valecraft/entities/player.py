'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 02:14:52
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, position: tuple[float, float], group: pygame.sprite.Group) -> None:
		super().__init__(group)
		self.image = pygame.Surface((16, 32))
		self.image.fill((255, 0, 0))
		self.rect: pygame.Rect = self.image.get_rect(center = position)
		self.direction = pygame.Vector2()
		self.position = pygame.Vector2(self.rect.center)
		self.speed = 200

	def input(self) -> None:
		keys = pygame.key.get_pressed()

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

	def move(self, dt: float) -> None:
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		self.position.x += self.direction.x * self.speed * dt
		self.rect.centerx = self.position.x

		self.position.y += self.direction.y * self.speed * dt
		self.rect.centery = self.position.y

	def update(self, dt: float):
		self.input()
		self.move(dt)