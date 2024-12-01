from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P8(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0, 0, "n1", hanging_ignore=True)
        n2 = Node(1, 0, "n2", hanging_ignore=True)
        n3 = Node(1, 1, "n3", hanging_ignore=True)
        n4 = Node(0, 1, "n4", hanging_ignore=True)
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(2, 0.5, "n6", hanging_ignore=True)
        n7 = Node(2, 1, "n7", hanging_ignore=True)
        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)
        g.add_edge(HyperEdge((n2, n5), "E"))
        g.add_edge(HyperEdge((n5, n3), "E"))
        g.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=False))
        g.add_edge(HyperEdge((n7, n3, n5, n6), "Q", rip=True))
        return g

    def get_right_side(self, left: Graph, lvl: int):
        n1, n2, n3, n4, n5, n6, n7, hn1, hn2, hQ1, hQ2 = left.ordered_nodes
        g = Graph()
        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)
        g.add_edge(HyperEdge((n2, n5), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n3), "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))
        g.add_edge(HyperEdge((n7, n3, n5, n6), "Q", rip=True))

        return g
