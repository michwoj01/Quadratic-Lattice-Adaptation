import math
from statistics import mean

from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge


@Production.register
class P11(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)

        g.add_edge(HyperEdge((n1, n7), "E"))
        g.add_edge(HyperEdge((n7, n2), "E"))
        g.add_edge(HyperEdge((n2, n5), "E"))
        g.add_edge(HyperEdge((n5, n3), "E"))
        g.add_edge(HyperEdge((n3, n4), "E"))
        g.add_edge(HyperEdge((n4, n6), "E"))
        g.add_edge(HyperEdge((n6, n8), "E"))
        g.add_edge(HyperEdge((n8, n1), "E"))
        g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "Q", rip=True))
        return g

    def get_right_side(self, left: Graph, lvl: int):
        # passed from above & updated with correct xy values
        n1, n2, n3, n4, n5, n6, n7, n8, hn1, hn2, hn3, hn4, hn5, hn6, hn7, hn8, hn9 = left.ordered_nodes

        g = Graph()
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7")
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8")
        n9 = Node(x=mean((n2.x, n5.x)), y=mean((n2.y, n5.y)), label=f"{lvl}n9", hanging=not hn3.hyperref.boundary)
        n10 = Node(x=mean((n3.x, n5.x)), y=mean((n3.y, n5.y)), label=f"{lvl}n10", hanging=not hn4.hyperref.boundary)
        n11 = Node(x=mean((n3.x, n4.x)), y=mean((n3.y, n4.y)), label=f"{lvl}n11", hanging=not hn5.hyperref.boundary)
        n12 = Node(x=mean((n4.x, n6.x)), y=mean((n4.y, n6.y)), label=f"{lvl}n12", hanging=not hn8.hyperref.boundary)
        n13 = Node(x=mean((n1.x, n2.x, n3.x, n4.x, n5.x, n6.x)),
                   y=mean((n1.y, n2.y, n3.y, n4.y, n5.y, n6.y)),
                   label=f"{lvl}n13")
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13]:
            g.add_node(n)

        # around the border
        g.add_edge(HyperEdge((n1, n7), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n7, n2), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n9), "E", boundary=hn3.hyperref.boundary))
        g.add_edge(HyperEdge((n9, n5), "E", boundary=hn3.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n10), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n10, n3), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n11), "E", boundary=hn5.hyperref.boundary))
        g.add_edge(HyperEdge((n11, n4), "E", boundary=hn5.hyperref.boundary))
        g.add_edge(HyperEdge((n4, n12), "E", boundary=hn6.hyperref.boundary))
        g.add_edge(HyperEdge((n12, n6), "E", boundary=hn6.hyperref.boundary))
        g.add_edge(HyperEdge((n6, n8), "E", boundary=hn8.hyperref.boundary))
        g.add_edge(HyperEdge((n8, n1), "E", boundary=hn8.hyperref.boundary))

        # to center hyper-node
        g.add_edge(HyperEdge((n7, n13), "E", boundary=False))
        g.add_edge(HyperEdge((n9, n13), "E", boundary=False))
        g.add_edge(HyperEdge((n10, n13), "E", boundary=False))
        g.add_edge(HyperEdge((n11, n13), "E", boundary=False))
        g.add_edge(HyperEdge((n12, n13), "E", boundary=False))
        g.add_edge(HyperEdge((n8, n13), "E", boundary=False))

        # Q-tag hyper-nodes
        g.add_edge(HyperEdge((n8, n1, n7, n13), "Q", boundary=False))
        g.add_edge(HyperEdge((n7, n2, n9, n13), "Q", boundary=False))
        g.add_edge(HyperEdge((n9, n5, n10, n13), "Q", boundary=False))
        g.add_edge(HyperEdge((n10, n3, n11, n13), "Q", boundary=False))
        g.add_edge(HyperEdge((n11, n4, n12, n13), "Q", boundary=False))
        g.add_edge(HyperEdge((n12, n6, n8, n13), "Q", boundary=False))

        return g
