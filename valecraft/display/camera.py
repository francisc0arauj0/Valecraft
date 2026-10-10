'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-10 00:47:51
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

from valecraft.entities.player import Player

class FarmCameraGroup(pygame.sprite.Group[pygame.sprite.Sprite]):
	def __init__(self) -> None:
		super().__init__()
		self.display = pygame.display.get_surface()
		self.offset = pygame.Vector2()
		self.zoom = 4

	def custom_draw(self, player: Player) -> None:
		if self.display:
			self.offset.x = (player.rect.centerx - self.display.get_width() / (2 * self.zoom))
			self.offset.y = (player.rect.centery - self.display.get_height() / (2 * self.zoom))

			for sprite in self.sprites():
				if sprite.image is None or sprite.rect  is None:
					continue
				image_scaled = pygame.transform.scale_by(sprite.image, self.zoom)
				offset_rect = image_scaled.get_rect(center = ((sprite.rect.centerx - self.offset.x) * self.zoom, (sprite.rect.centery - self.offset.y) * self.zoom))
				self.display.blit(image_scaled, offset_rect)