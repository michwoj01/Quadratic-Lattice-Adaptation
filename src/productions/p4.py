from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P4(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(0, 0.5, "n6", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n2), "E"))
        g.add_edge(HyperEdge((n2, n5), "E"))
        g.add_edge(HyperEdge((n5, n3), "E"))
        g.add_edge(HyperEdge((n3, n4), "E"))
        g.add_edge(HyperEdge((n4, n6), "E"))
        g.add_edge(HyperEdge((n6, n1), "E"))

        g.add_edge(HyperEdge((n1, n2, n3, n4), "Q", rip=True))
        return g

    def get_right_side(self, left: Graph, lvl: int) -> Graph:
        n1, n2, n3, n4, old_n5, old_n6, hn1n2, hn2n5, hn5n3, hn3n4, hn4n6, hn6n1, _ = left.ordered_nodes
        g = Graph()
        n7 = Node((n1.x + n2.x)/2, (n1.y + n2.y)/2, f"{lvl}n7", hanging=not hn1n2.hyperref.boundary)
        n8 = Node((n3.x + n4.x)/2, (n3.y + n4.y)/2, f"{lvl}n8", hanging=not hn3n4.hyperref.boundary)
        n9 = Node((n1.x + n2.x + n3.x + n4.x)/4, (n1.x + n2.x + n3.x + n4.x)/4, f"{lvl}n9")
        
        n5 = Node(old_n5.x, old_n5.y, old_n5.label)
        n6 = Node(old_n6.x, old_n6.y, old_n6.label)


        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n7), "E", boundary=hn1n2.hyperref.boundary))
        g.add_edge(HyperEdge((n7, n2), "E", boundary=hn1n2.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n5), "E", boundary=hn2n5.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n3), "E", boundary=hn5n3.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n8), "E", boundary=hn3n4.hyperref.boundary))
        g.add_edge(HyperEdge((n8, n4), "E", boundary=hn3n4.hyperref.boundary))
        g.add_edge(HyperEdge((n4, n6), "E", boundary=hn4n6.hyperref.boundary))
        g.add_edge(HyperEdge((n6, n1), "E", boundary=hn6n1.hyperref.boundary))
        
        g.add_edge(HyperEdge((n6, n9), "E"))
        g.add_edge(HyperEdge((n5, n9), "E"))
        g.add_edge(HyperEdge((n8, n9), "E"))
        g.add_edge(HyperEdge((n7, n9), "E"))

        g.add_edge(HyperEdge((n1, n7, n9, n6), "Q"))
        g.add_edge(HyperEdge((n7, n2, n5, n9), "Q"))
        g.add_edge(HyperEdge((n9, n5, n3, n8), "Q"))
        g.add_edge(HyperEdge((n6, n9, n8, n4), "Q"))
        return g
