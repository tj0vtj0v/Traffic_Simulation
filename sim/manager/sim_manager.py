from pygame.surface import Surface

from sim.manager.sim_monitor import SimMonitor
from sim.manager.sim_object_manager import SimObjectManager


class SimManager(SimMonitor):
    def __init__(self, canvas: Surface):
        super().__init__(canvas)
        self.canvas = canvas

    def start_simulation(self):
        self.add_sim_objects()

    def simulation_management(self):
        pass

    def sim_loop_update(self):
        self.update_sim_objects()
        self.simulation_management()
