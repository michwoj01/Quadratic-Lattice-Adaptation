from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    x: float
    y: float
    h: bool

    def copy(self):
        return Node(self.x, self.y, self.h)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, value: object) -> bool:
        return value and self.x == value.x and self.y == value.y
