from pygame.surface import Surface

from sim.manager.sim_object_manager import SimObjectManager


class SimMonitor(SimObjectManager):
    def __init__(self, canvas: Surface):
        super().__init__(canvas)
