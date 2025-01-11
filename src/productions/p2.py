from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P2(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        n5 = Node(0.5, 0, "n5", hanging=True) 
        for n in [n1, n2, n3, n4, n5]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n5), "E"))
        g.add_edge(HyperEdge((n5, n2), "E"))
        g.add_edge(HyperEdge((n2, n3), "E"))
        g.add_edge(HyperEdge((n3, n4), "E"))
        g.add_edge(HyperEdge((n4, n1), "E"))

        g.add_edge(HyperEdge((n1, n2, n3, n4), "Q", rip=True))  # Rip flag for refinement
        return g

    def get_right_side(self, left: Graph, lvl: int):
        n1, n2, n3, n4, old_n5, n1n5, n5n2, n2n3, n3n4, n4n1, _  = left.ordered_nodes
        g = Graph()

        n5 = old_n5.with_hanging_false()
        n6 = Node((n2.x + n3.x)/2, (n2.y + n3.y)/2, f"{lvl}n6", hanging=not n2n3.hyperref.boundary)
        n7 = Node((n3.x + n4.x)/2, (n3.y + n4.y)/2, f"{lvl}n7", hanging=not n3n4.hyperref.boundary)
        n8 = Node((n4.x + n1.x)/2, (n4.y + n1.y)/2, f"{lvl}n8", hanging=not n4n1.hyperref.boundary)
        n9 = Node((n1.x + n2.x + n3.x + n4.x)/4, (n1.y + n2.y + n3.y + n4.y)/4, f"{lvl}n9")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n5), "E", boundary=n1n5.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n2), "E", boundary=n5n2.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n6), "E", boundary=n2n3.hyperref.boundary))
        g.add_edge(HyperEdge((n6, n3), "E", boundary=n2n3.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n7), "E", boundary=n3n4.hyperref.boundary))
        g.add_edge(HyperEdge((n7, n4), "E", boundary=n3n4.hyperref.boundary))
        g.add_edge(HyperEdge((n4, n8), "E", boundary=n4n1.hyperref.boundary))
        g.add_edge(HyperEdge((n8, n1), "E", boundary=n4n1.hyperref.boundary))

        g.add_edge(HyperEdge((n5, n9), "E"))
        g.add_edge(HyperEdge((n6, n9), "E"))
        g.add_edge(HyperEdge((n7, n9), "E"))
        g.add_edge(HyperEdge((n8, n9), "E"))

        g.add_edge(HyperEdge((n1, n5, n9, n8), "Q"))
        g.add_edge(HyperEdge((n5, n2, n6, n9), "Q"))
        g.add_edge(HyperEdge((n8, n9, n7, n4), "Q"))
        g.add_edge(HyperEdge((n9, n6, n3, n7), "Q"))

        return g