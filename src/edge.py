from dataclasses import dataclass
from node import Node
from typing import List

@dataclass(frozen=True)
class Edge:
    nodes: tuple[Node, Node]
    label: str
    b: bool | None
    r: bool | None

    def copy_with_different_point(self, u, v):
        return Edge((u, v), self.label, self.b, self.r)