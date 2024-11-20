from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P6(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0, 0, "n1", hanging=False)
        n2 = Node(1, 0, "n2", hanging=False)
        n3 = Node(1, 1, "n3", hanging=False)
        n4 = Node(0, 1, "n4", hanging=False)
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(0.5, 0, "n6", hanging=True)
        n7 = Node(0, 0.5, "n7", hanging=True)
        n8 = Node(0.5, 1, "n8", hanging=True)
        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)
        g.add_edge(HyperEdge((n1, n6), "E"))
        g.add_edge(HyperEdge((n6, n2), "E"))
        g.add_edge(HyperEdge((n2, n5), "E"))
        g.add_edge(HyperEdge((n5, n3), "E"))
        g.add_edge(HyperEdge((n3, n8), "E"))
        g.add_edge(HyperEdge((n8, n4), "E"))
        g.add_edge(HyperEdge((n4, n7), "E"))
        g.add_edge(HyperEdge((n7, n1), "E"))
        g.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))
        return g

    def get_right_side(self, left: Graph, lvl: int):
        # passed from above & updated with correct xy values
        n1, n2, n3, n4, n5, n6, n7, n8, hn1, hn2, hn3, hn4, hn5, hn6, hn7, hn8, hQ = left.ordered_nodes
        g = Graph()
        n5 = Node(n5.x, n5.y, "n5", hanging=False)
        n6 = Node(n6.x, n6.y, "n6", hanging=False)
        n7 = Node(n7.x, n7.y, "n7", hanging=False)
        n8 = Node(n8.x, n8.y, "n8", hanging=False)
        n9 = Node((n1.x+n2.x+n3.x+n4.x)/4, (n1.y+n2.y+n3.y+n4.y)/4, f"{lvl}n9")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        # border of graph
        g.add_edge(HyperEdge((n1, n6), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n6, n2), "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n5), "E", boundary=hn3.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n3), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n8), "E", boundary=hn5.hyperref.boundary))
        g.add_edge(HyperEdge((n8, n4), "E", boundary=hn6.hyperref.boundary))
        g.add_edge(HyperEdge((n4, n7), "E", boundary=hn7.hyperref.boundary))
        g.add_edge(HyperEdge((n7, n1), "E", boundary=hn8.hyperref.boundary))

        # to center hyper-node
        g.add_edge(HyperEdge((n5, n9), "E", boundary=False))
        g.add_edge(HyperEdge((n6, n9), "E", boundary=False))
        g.add_edge(HyperEdge((n7, n9), "E", boundary=False))
        g.add_edge(HyperEdge((n8, n9), "E", boundary=False))

        # Q-tag hyper-nodes
        g.add_edge(HyperEdge((n1, n6, n9, n7), "Q", rip=False))
        g.add_edge(HyperEdge((n6, n2, n5, n9), "Q", rip=False))
        g.add_edge(HyperEdge((n5, n9, n3, n8), "Q", rip=False))
        g.add_edge(HyperEdge((n8, n4, n7, n9), "Q", rip=False))

        return g
