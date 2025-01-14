from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P21(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0.2,0 , "n1", hanging_ignore=True)
        n2 = Node(1, 0, "n2", hanging_ignore=True)
        n3 = Node(1, 1, "n3", hanging_ignore=True)
        n4 = Node(0.2, 1, "n4", hanging_ignore=True)
        n5 = Node(0, 0.5, "n5", hanging_ignore=True)
        n6 = Node(0.6, 0, "n6", hanging_ignore=True)

        for n in [n1, n2, n3, n4, n5, n6]:
            g.add_node(n)

        g.add_edge(HyperEdge((n3, n4, n1, n2, n5,n6), "S", rip=False))
        return g

    def get_right_side(self, left: Graph, lvl: int):
        n1, n2, n3, n4, n5, n6, hn1 = left.ordered_nodes
        g = Graph()
        for n in [n1, n2, n3, n4, n5, n6]:
            g.add_node(n)
        
        g.add_edge(HyperEdge((n3, n4, n1, n2, n5,n6), "S", rip=True))
        return g
