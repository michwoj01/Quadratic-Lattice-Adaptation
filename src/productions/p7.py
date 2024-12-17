from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P7(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0, 0, "n1", hanging_ignore=True)
        n2 = Node(1, 0, "n2", hanging_ignore=True)
        n3 = Node(1, 1, "n3", hanging_ignore=True)
        n4 = Node(0, 1, "n4", hanging_ignore=True)

        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n2, n3, n4), "Q"))
        return g

    def get_right_side(self, left: Graph, lvl: int) -> Graph:
        n1, n2, n3, n4, _ = left.ordered_nodes
        g = Graph()

        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n2, n3, n4), "Q", rip=True))
        return g
