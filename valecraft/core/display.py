'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-07 17:56:10
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

import pygame

class Display:
    def __init__(self) -> None:
        self.window_size = (800, 600)

        self.screen = pygame.display.set_mode(self.window_size,pygame.RESIZABLE)
        pygame.display.set_caption("Valecraft")

        self.is_fullscreen = False

    def toggle_fullscreen(self) -> None:
        self.is_fullscreen = not self.is_fullscreen

        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

    def resize(self, size: tuple[int, int]) -> None:
        if not self.is_fullscreen:
            self.window_size = size
            self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)