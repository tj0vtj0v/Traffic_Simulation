import pygame
from pygame.surface import Surface


class InputManager:
    def __init__(self, canvas: Surface):
        self.running = True
        self.canvas = canvas

    def sim_loop_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
