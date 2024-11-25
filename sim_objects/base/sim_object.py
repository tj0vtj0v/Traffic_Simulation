from abc import ABC, abstractmethod

from pygame import draw
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
    def __init__(
            self,
            canvas: Surface,
            position: Position = Position(0, 0),
            distance_to_background: int = 0,
            rotation: float = 0,
            size: float = 1):
        self._canvas = canvas
        self._position = position
        self._distance_to_background = distance_to_background
        self._rotation = rotation
        self._size = size

    @abstractmethod
    def update_status(self):
        pass

    @abstractmethod
    def update_position(self):
        pass

    @abstractmethod
    def add_to_canvas(self):
        draw.circle(self._canvas, (255, 255, 255), self._position.get_position(), 5)
