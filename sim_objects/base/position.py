from pygame.math import Vector2

from utils.double_linked_list import DoubleLinkedList


class Position:
    __x: float
    __y: float
    __waypoints: DoubleLinkedList
    __direction_vector: Vector2

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__waypoints = DoubleLinkedList()

    def get_position(self) -> tuple[int, int]:
        return round(self.__x), round(self.__y)

    def up(self, pixel: float = 1):
        self.__y -= pixel

    def down(self, pixel: float = 1):
        self.__y += pixel

    def left(self, pixel: float = 1):
        self.__x -= pixel

    def right(self, pixel: float = 1):
        self.__x += pixel

    def get_direction_vector(self) -> Vector2:
        if self.__waypoints.empty():
            return Vector2(0, 0)

        current_waypoint = self.__waypoints.first()
        return Vector2(
            current_waypoint.__x - self.__x,
            current_waypoint.__y - self.__y
        )

    def add_waypoint(self, waypoint: "Position"):
        self.__waypoints.append(waypoint)

    def target_next_waypoint(self):
        self.__waypoints.pop_first()

    def last_waypoint(self):
        return self.__waypoints.length() == 1

    def is_at_waypoint(self) -> bool:
        if self.__waypoints.empty():
            return True

        return self.__eq__(self.__waypoints.first())

    def move_to_waypoint(self, distance: float) -> None:
        if self.__waypoints.empty():
            return

        direction_vector = self.get_direction_vector()

        if direction_vector.length() > distance:
            direction_vector.scale_to_length(distance)

        self.__x += direction_vector.x
        self.__y += direction_vector.y

    def distance_to_waypoint(self) -> float:
        if self.__waypoints.empty():
            return 0.0

        return self.get_direction_vector().length()

    def __eq__(self, other: "Position") -> bool:
        return (
                abs(abs(self.__x) - abs(other.__x)) <= .5 and
                abs(abs(self.__y) - abs(other.__y)) <= .5
        )

    def __ne__(self, other: "Position") -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return f"Position at ({self.__x}, {self.__y})"
