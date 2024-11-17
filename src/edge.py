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


@dataclass(frozen=True)
class HyperEdge:
    nodes: Set[Node]
    label: str
    b: bool | None
    r: bool | None
