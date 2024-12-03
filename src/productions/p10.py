from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge
import math

@Production.register
class P10(Production):
    def get_left_side(self) -> Graph:
       
        g = Graph()
        n1 = Node(0.25, 0, "n1")
        n2 = Node(0.75, 0, "n2")
        n3 = Node(0.75, 2*math.sqrt(0.25), "n3")
        n4 = Node(0.25, 2*math.sqrt(0.25), "n4")
        n5 = Node(1, math.sqrt(0.25), "n5")
        n6 = Node(0, math.sqrt(0.25), "n6")
        n7 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, "n7", hanging=True)

        e1 = HyperEdge((n1, n7), "E")
        e2 = HyperEdge((n7, n2), "E")
        e3 = HyperEdge((n2, n5), "E")
        e4 = HyperEdge((n4, n3), "E")
        e5 = HyperEdge((n6, n4), "E")
        e6 = HyperEdge((n6, n1), "E")
        e7 = HyperEdge((n3, n5), "E")
        
        e8 = HyperEdge((n3, n4, n1, n2, n5 ,n6), "S", rip=True)
        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        
        return g

    def get_right_side(self, left: Graph, lvl: int):
        # passed from above & updated with correct xy values
        n1, n2, n3, n4, n5, n6,  n7,  hn1, hn2, hn3, hn4, hn5, hn6 , hn7 , hn8= left.ordered_nodes
        g = Graph()
        n7 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, "n7", hanging=False)
        n8 = Node((n2.x+n5.x)/2, (n2.y+n5.y)/2, f"{lvl}n8", hanging=not hn2.hyperref.boundary)
        n9 = Node((n6.x+n4.x)/2, (n6.y+n4.y)/2, f"{lvl}n9", hanging=not hn5.hyperref.boundary)
        n10 = Node((n6.x+n1.x)/2, (n6.y+n1.y)/2, f"{lvl}n10", hanging=not hn6.hyperref.boundary)
        n11 = Node((n4.x+n3.x)/2, (n4.y+n3.y)/2, f"{lvl}n11", hanging=not hn4.hyperref.boundary)
        n12 = Node((n5.x+n3.x)/2, (n5.y+n3.y)/2, f"{lvl}n12", hanging=not hn3.hyperref.boundary)
      
        n13 = Node((n1.x+n2.x+n3.x+n4.x+ n5.x + n6.x)/6, (n1.y+n2.y+n3.y+n4.y+ n5.y + n6.y)/6, f"{lvl}n13")
        
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13]:
            g.add_node(n)

        # around the border
        g.add_edge(HyperEdge((n13, n7),  "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n13, n8),  "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n13, n9),  "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n13, n10), "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n13, n11), "E", boundary=hn3.hyperref.boundary))
        g.add_edge(HyperEdge((n13, n12), "E", boundary=hn3.hyperref.boundary))
     
        g.add_edge(HyperEdge((n1, n7),  "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n10, n1), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n10, n6), "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n6, n9),  "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n9, n4),  "E", boundary=hn5.hyperref.boundary))
        g.add_edge(HyperEdge((n4, n11), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n11, n3), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n12), "E", boundary=hn3.hyperref.boundary))

        g.add_edge(HyperEdge((n12, n5), "E", boundary=hn3.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n8),  "E", boundary=hn5.hyperref.boundary))
        g.add_edge(HyperEdge((n8, n2),  "E", boundary=hn6.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n7),  "E", boundary=hn6.hyperref.boundary))
          

        # Q-tag hyper-nodes
        g.add_edge(HyperEdge((n1, n7, n10, n13), "Q", rip=False))
        g.add_edge(HyperEdge((n2, n7, n8, n13),  "Q", rip=False))
        g.add_edge(HyperEdge((n5, n8, n12, n13), "Q", rip=False))
        g.add_edge(HyperEdge((n3, n11, n12, n13),"Q", rip=False))
        g.add_edge(HyperEdge((n4, n9, n11, n13), "Q", rip=False))
        g.add_edge(HyperEdge((n6, n9, n10, n13), "Q", rip=False))

        return g