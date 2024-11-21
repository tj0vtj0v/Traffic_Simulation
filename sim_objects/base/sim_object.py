from abc import ABC, abstractmethod

from pygame.surface import Surface

from sim_objects.base.position import Position


class SimObject(ABC):
    _canvas: Surface
    _position: Position
    _distance_to_background: int
    _rotation: float
    _size: float
    _width: float
    _height: float

    @abstractmethod
    def update_status(self):
        pass

    @abstractmethod
    def update_position(self):
        pass

    @abstractmethod
    def add_to_canvas(self):
        pass
