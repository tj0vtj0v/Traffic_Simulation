from pygame.surface import Surface

from sim.manager.input_manager import InputManager


class WorldManager(InputManager):
    def __init__(self, canvas: Surface):
        super().__init__(canvas)

    def build_world(self):
        pass
