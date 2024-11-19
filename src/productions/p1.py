from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P1Example(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        for n in [n1, n2, n3, n4]:
            g.add_node(n)
        g.add_edge(HyperEdge((n1, n2), "E"))
        g.add_edge(HyperEdge((n1, n4), "E"))
        g.add_edge(HyperEdge((n2, n3), "E"))
        g.add_edge(HyperEdge((n4, n3), "E"))
        g.add_edge(HyperEdge((n3, n4, n1, n2), "Q"))
        return g

    def get_right_side(self, left: Graph, lvl: int):
        # passed from above & updated with correct xy values
        n1, n2, n3, n4 = left.normal_nodes
        g = Graph()
        n5 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, f"{lvl}n5")
        n6 = Node((n2.x+n3.x)/2, (n2.y+n3.y)/2, f"{lvl}n6")
        n7 = Node((n3.x+n4.x)/2, (n3.y+n4.y)/2, f"{lvl}n7")
        n8 = Node((n4.x+n1.x)/2, (n4.y+n1.y)/2, f"{lvl}n8")
        n9 = Node((n1.x+n2.x+n3.x+n4.x)/4, (n1.y+n2.y+n3.y+n4.y)/4, f"{lvl}n9")
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)
        g.add_edge(HyperEdge((n1, n5), "E"))
        g.add_edge(HyperEdge((n5, n2), "E"))
        g.add_edge(HyperEdge((n1, n8), "E"))
        g.add_edge(HyperEdge((n5, n9), "E"))
        g.add_edge(HyperEdge((n2, n6), "E"))
        g.add_edge(HyperEdge((n8, n9), "E"))
        g.add_edge(HyperEdge((n9, n6), "E"))
        g.add_edge(HyperEdge((n8, n4), "E"))
        g.add_edge(HyperEdge((n9, n7), "E"))
        g.add_edge(HyperEdge((n6, n3), "E"))
        g.add_edge(HyperEdge((n4, n7), "E"))
        g.add_edge(HyperEdge((n7, n3), "E"))
        g.add_edge(HyperEdge((n1, n5, n9, n8), "Q"))
        g.add_edge(HyperEdge((n5, n2, n6, n9), "Q"))
        g.add_edge(HyperEdge((n8, n9, n7, n4), "Q"))
        g.add_edge(HyperEdge((n9, n6, n3, n7), "Q"))

        return g
