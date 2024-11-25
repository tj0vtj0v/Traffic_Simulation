from abc import ABC

from pygame import Surface

from sim_objects.base.position import Position
from sim_objects.base.sim_object import SimObject


class PathBlockingSimObject(SimObject, ABC):
    def __init__(
            self,
            canvas: Surface,
            position: Position = Position(0, 0),
            distance_to_background: int = 0,
            rotation: float = 0,
            size: float = 1):
        super().__init__(canvas, position, distance_to_background, rotation, size)
