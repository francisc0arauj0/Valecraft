'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 18:17:00
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

from pathlib import Path

import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self, position: tuple[float, float], group: pygame.sprite.Group[pygame.sprite.Sprite], sprite_name: str = "default") -> None:
		super().__init__(group)

		self.direction = pygame.Vector2()
		self.speed = 0

		sprite_path = Path(Path(__file__).resolve().parents[2]/"assets"/"graphics"/f"{sprite_name}"/f"{sprite_name}.png")
		self.spritesheet = pygame.image.load(str(sprite_path)).convert_alpha()
		self.images = {
			"right": self.spritesheet.subsurface(pygame.Rect(0, 0, 16, 16)).copy(),
            "left": self.spritesheet.subsurface(pygame.Rect(0, 16, 16, 16)).copy(),
            "down": self.spritesheet.subsurface(pygame.Rect(0, 32, 16, 16)).copy(),
            "up": self.spritesheet.subsurface(pygame.Rect(0, 48, 16, 16)).copy(),
            "hit": self.spritesheet.subsurface(pygame.Rect(16, 0, 16, 16)).copy(),
		}
		self.state = "down"
		self.image = self.images[self.state]

		self.image = pygame.Surface((24, 32))
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
		self.move(dt)