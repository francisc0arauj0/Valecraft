
'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-10 00:47:51
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

from valecraft.entities.entity import Entity


class CameraGroup(pygame.sprite.Group[pygame.sprite.Sprite]):
	def __init__(self) -> None:
		super().__init__()

		self.display = pygame.display.get_surface()
		self.offset = pygame.Vector2()

		if self.display:
			self.half_width = self.display.get_width() / 2
			self.half_height = self.display.get_height() / 2
			self.internal_display_size = self.display.get_size()
		else:
			self.half_width = 0
			self.half_height = 0
			self.internal_display_size = (800, 600)

		self.internal_display = pygame.Surface(self.internal_display_size, pygame.SRCALPHA)

		self.zoom_levels = [2, 3, 4]
		self.zoom_index = 0
		self.zoom_scale = self.zoom_levels[self.zoom_index]

		self.zoom_cooldown = 0.2
		self.zoom_timer = 0.0

	def center_target_camera(self, target: Entity) -> None:
		self.offset.x = target.rect.centerx - self.half_width
		self.offset.y = target.rect.centery - self.half_height

	def zoom_control(self, dt: float) -> None:
		self.zoom_timer += dt

		if self.zoom_timer < self.zoom_cooldown:
			return

		keys = pygame.key.get_pressed()

		if not keys[pygame.K_LCTRL]:
			return

		if keys[pygame.K_EQUALS] or keys[pygame.K_PLUS]:
			self.zoom_index = min(self.zoom_index + 1, len(self.zoom_levels) - 1)
		elif keys[pygame.K_MINUS]:
			self.zoom_index = max(self.zoom_index - 1, 0)
		else:
			return

		self.zoom_scale = self.zoom_levels[self.zoom_index]
		self.zoom_timer = 0.0

	def resize(self, size: tuple[int, int]) -> None:
		self.display = pygame.display.get_surface()

		self.half_width = size[0] / 2
		self.half_height = size[1] / 2

		self.internal_display_size = size
		self.internal_display = pygame.Surface(size, pygame.SRCALPHA)

	def update(self, dt: float) -> None:
		self.zoom_control(dt)

	def custom_draw(self, target: Entity) -> None:
		if not self.display:
			return

		self.center_target_camera(target)
		self.internal_display.fill((0, 0, 0))

		for sprite in self.sprites():
			if sprite.image is None or sprite.rect is None:
				continue

			offset_position = (pygame.Vector2(sprite.rect.topleft) - self.offset)
			self.internal_display.blit(sprite.image, offset_position)

		scaled_size = (
			max(1, int(self.internal_display_size[0] * self.zoom_scale)),
			max(1, int(self.internal_display_size[1] * self.zoom_scale))
		)

		scaled_display = pygame.transform.scale(self.internal_display, scaled_size)
		scaled_rect = scaled_display.get_rect(center=(self.half_width, self.half_height))

		self.display.blit(scaled_display, scaled_rect)
