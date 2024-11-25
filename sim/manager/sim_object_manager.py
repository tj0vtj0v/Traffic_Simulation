from pygame.surface import Surface

from sim_objects.base.position import Position
from sim_objects.base.sim_object import SimObject
from sim_objects.movable.car import Car
from utils.double_linked_list import DoubleLinkedList


class SimObjectManager:
    sim_objects: DoubleLinkedList

    def __init__(self, canvas: Surface):
        self.canvas = canvas
        self.sim_objects = DoubleLinkedList()

    def add_sim_object(self, sim_object: SimObject):
        self.sim_objects.append(sim_object)

    def add_sim_objects(self):
        self.sim_objects.setup(
            Car(self.canvas)
        )

    def update_sim_objects(self):
        for sim_object in self.sim_objects:
            sim_object.update_status()
            sim_object.update_position()
            sim_object.add_to_canvas()
