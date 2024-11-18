from dataclasses import dataclass
from typing import Set

from node import Node


@dataclass(frozen=True)
class Edge:
    nodes: tuple[Node, Node]
    label: str
    b: bool | None
    r: bool | None

    def copy_with_different_point(self, u, v):
        return Edge((u, v), self.label, self.b, self.r)

    def __hash__(self) -> int:
        return hash(set(self.nodes))

    def __eq__(self, value: object) -> bool:
        return value and set(self.nodes) == set(value.nodes)


@dataclass(frozen=True)
class HyperEdge:
    nodes: tuple[Node, ...]
    label: str
    b: bool | None
    r: bool | None

    def __hash__(self) -> int:
        return hash(self.nodes)

    def __eq__(self, value: object) -> bool:
        return value and self.nodes == value.nodes
