'''
 # @ Author: Francisco Araújo
 # @ Create Time: 2026-10-08 00:46:23
 # @ Copyright: Copyright (c) 2026 Francisco Araújo
 '''

from valecraft.scene.farm import Farm

class SceneManager:
	def __init__(self, scene: str) -> None:
		if scene == "farm":
			self.current_scene = Farm()

	def update(self, dt: float) -> None:
		self.current_scene.update(dt)

	def draw(self) -> None:
		self.current_scene.draw()