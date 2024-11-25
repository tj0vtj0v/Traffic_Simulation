import pygame
from pygame.surface import Surface

from sim.manager.sim_manager import SimManager


class InputManager:
    def __init__(self, canvas: Surface):
        self.running = True
        self.canvas = canvas

        self.sim_manager = SimManager(self.canvas)

    def sim_loop_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
