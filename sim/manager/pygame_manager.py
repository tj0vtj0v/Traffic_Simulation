import pygame

from sim.manager.sim_manager import SimManager
from sim.manager.world_manager import WorldManager


class PygameManager(WorldManager):
    def __init__(self):
        super().__init__(pygame.display.set_mode((920, 920)))

        self.clock = pygame.time.Clock()
        self.sim_manager = SimManager(self.canvas)

    def start(self) -> None:
        pygame.init()

        self.sim_setup()

        self.sim_loop()

        pygame.quit()

    def sim_setup(self):
        self.build_world()
        self.sim_manager.start_simulation()

    def sim_loop(self):
        while self.running:
            self.sim_loop_update()

    def sim_loop_update(self):
        self.canvas.fill((0, 0, 0))

        super().sim_loop_update()
        self.sim_manager.sim_loop_update()

        pygame.display.flip()
        self.clock.tick(120)
