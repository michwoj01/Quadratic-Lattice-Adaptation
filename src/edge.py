from dataclasses import dataclass
from node import Node

@dataclass(frozen=True)
class HyperEdge:
    nodes: tuple[Node, ...]
    label: str
    boundary: bool = False
    rip: bool = False

    def get_hypernode(self):
        # get networkx node that will represent this hyper-edge
        # place simulated node at the average of all connecting nodes
        x = sum([node.x for node in self.nodes]) / len(self.nodes)
        y = sum([node.y for node in self.nodes]) / len(self.nodes)

        # create unique node label
        label = self.label
        for node in self.nodes:
            label += node.label

        return Node(x, y, label, hanging=False, hyper=True, hypertag=self.label)
