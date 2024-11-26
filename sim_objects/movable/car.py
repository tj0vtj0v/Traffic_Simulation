from pygame import Surface, draw

from sim_objects.base.path_blocking_sim_object import PathBlockingSimObject
from sim_objects.base.position import Position


class Car(PathBlockingSimObject):
    __speed: float = 0
    __acceleration: float
    __top_speed: float
    __has_to_stop: bool
    __color: tuple[int, int, int]

    def __init__(
            self,
            canvas: Surface,
            position: Position = Position(0, 0),
            distance_to_background: int = 0,
            rotation: float = 0,
            size: float = 1):
        super().__init__(canvas, position, distance_to_background, rotation, size)

        self.__top_speed = 3
        self.__acceleration = .01
        self.__has_to_stop = False
        self.__color = (255, 255, 255)
        self._position.add_waypoint(Position(500, 300))
        self._position.add_waypoint(Position(800, 700))
        self._position.add_waypoint(Position(100, 700))

    def update_status(self):
        if self._position.last_waypoint() and (self.breaking_distance() >= self._position.distance_to_waypoint() > 0):
            self.__has_to_stop = True
        if self.__speed == 0:
            self.__has_to_stop = False

        if self.__has_to_stop:
            self.__speed -= self.__acceleration
            if self.__speed < 0:
                self.__speed = 0
            self.__color = (255, 0, 0)
        elif self.__speed < self.__top_speed and not self._position.is_at_waypoint():
            self.__speed += self.__acceleration
            self.__color = (0, 255, 0)
        else:
            self.__speed = self.__top_speed
            self.__color = (255, 255, 255)

    def breaking_distance(self) -> float:
        return ((self.__speed + self.__acceleration) ** 2) / (self.__acceleration * 2) - (
                    self.__speed + self.__acceleration)

    def update_position(self):
        if self._position.is_at_waypoint():
            self._position.target_next_waypoint()
        self._position.move_to_waypoint(self.__speed)

    def add_to_canvas(self):
        draw.circle(self._canvas, self.__color, self._position.get_position(), 5)

        v = self._position.get_direction_vector()
        if not v.length() == 0:
            v.scale_to_length(self.breaking_distance())
        x, y = self._position.get_position()[0] + v.x, self._position.get_position()[1] + v.y
        draw.line(self._canvas, (0, 0, 255), self._position.get_position(), (x, y))

        draw.circle(self._canvas, (0, 255, 255), (500, 300), 2)
        draw.circle(self._canvas, (0, 255, 255), (800, 700), 2)
        draw.circle(self._canvas, (0, 255, 255), (100, 700), 2)
