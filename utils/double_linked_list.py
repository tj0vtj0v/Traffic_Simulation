from typing import TypeVar, Iterator

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node | None = None
        self.prev: Node | None = None


class DoubleLinkedList:
    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__size = 0

    def length(self):
        return self.__size

    def empty(self) -> bool:
        return self.__size == 0

    def setup(self, *data: T) -> None:
        for entry in data:
            self.append(entry)

    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size += 1

    def pop_first(self) -> T:
        if self.__head is None:
            return None

        tmp = self.__head

        if self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

        self.__size -= 1
        return tmp.data

    def first(self) -> T:
        if self.__head is None:
            return None

        return self.__head.data

    def __iter__(self) -> Iterator[T]:
        current = self.__head
        while current is not None:
            yield current.data
            current = current.next
